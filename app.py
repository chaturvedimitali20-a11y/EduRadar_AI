import re
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Auto-creates a real SQL database file (eduradar.db) automatically!
def init_db():
    conn = sqlite3.connect("eduradar.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scan_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            branch TEXT,
            target_role TEXT,
            ats_score INTEGER,
            keyword_score INTEGER,
            format_score INTEGER,
            scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

STOP_WORDS = {
    'and', 'the', 'to', 'of', 'in', 'a', 'for', 'with', 'on', 'as', 'is', 'are',
    'will', 'be', 'or', 'an', 'at', 'by', 'from', 'that', 'this', 'we', 'you',
    'your', 'our', 'have', 'has', 'experience', 'work', 'working', 'skills', 'team',
    'strong', 'looking', 'plus', 'using', 'based', 'role', 'candidate', 'required'
}

ACTION_VERBS = {
    'developed', 'built', 'designed', 'implemented', 'optimized', 'created',
    'managed', 'led', 'engineered', 'analyzed', 'deployed', 'automated', 'improved'
}

def analyze_resume(resume_text, jd_text):
    resume_clean = resume_text.lower()
    jd_clean = jd_text.lower()

    jd_words = set(re.findall(r'\b[a-zA-Z0-9+#]{2,}\b', jd_clean)) - STOP_WORDS
    resume_words = set(re.findall(r'\b[a-zA-Z0-9+#]{2,}\b', resume_clean))

    found_keywords = sorted(list(jd_words.intersection(resume_words)))
    missing_keywords = sorted(list(jd_words - resume_words))

    keyword_score = min(int((len(found_keywords) / max(len(jd_words), 1)) * 100), 100)
    verbs_used = ACTION_VERBS.intersection(resume_words)
    verb_score = min(int((len(verbs_used) / 4) * 100), 100)

    tips = []
    format_score = 0
    if '@' in resume_clean:
        format_score += 35
    else:
        tips.append("Include a professional email address at the top of your resume.")

    if len(resume_text.split()) >= 40:
        format_score += 35
    else:
        tips.append("Expand your project bullet points with measurable technical details.")

    if any(h in resume_clean for h in ['education', 'skills', 'projects', 'experience']):
        format_score += 30
    else:
        tips.append("Add clear standard headers: Education, Skills, Projects, Experience.")

    ats_score = int((keyword_score * 0.55) + (verb_score * 0.25) + (format_score * 0.20))

    return {
        'ats_score': ats_score,
        'keyword_score': keyword_score,
        'verb_score': verb_score,
        'format_score': format_score,
        'found_keywords': found_keywords[:20],
        'missing_keywords': missing_keywords[:20],
        'tips': tips
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    student_name = request.form.get('student_name', 'Mitali Chaturvedi')
    branch = request.form.get('branch', 'CSE')
    target_role = request.form.get('target_role', 'Software Developer Intern')
    resume_text = request.form.get('resume_text', '')
    jd_text = request.form.get('jd_text', '')

    results = analyze_resume(resume_text, jd_text)

    conn = sqlite3.connect("eduradar.db")
    conn.execute(
        "INSERT INTO scan_history (student_name, branch, target_role, ats_score, keyword_score, format_score) VALUES (?, ?, ?, ?, ?, ?)",
        (student_name, branch, target_role, results['ats_score'], results['keyword_score'], results['format_score'])
    )
    conn.commit()
    conn.close()

    return render_template('result.html', student_name=student_name, target_role=target_role, **results)

@app.route('/admin')
def admin():
    conn = sqlite3.connect("eduradar.db")
    conn.row_factory = sqlite3.Row
    scans = conn.execute("SELECT * FROM scan_history ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('admin.html', scans=scans)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=False)
