# EduRadar AI — Student Career Readiness & ATS Optimization Portal

**Competition:** PRASUNEX INNOVATHON 2026 (Round 3 Working Prototype)  
**Innovator:** Mitali Chaturvedi (Solo Participant)

---

## 📌 Problem & Solution
Up to **75% of student resumes** are filtered out by corporate Applicant Tracking Systems (ATS) before reaching a human recruiter. **EduRadar AI** is a lightweight, ERP-ready web module built to integrate seamlessly into the **PRASUNEX Education Management Platform**, empowering students to benchmark their resumes against live job descriptions and enabling placement cells to track institutional readiness.

## ✨ Implemented Features
- **Student Career Readiness Scanner (`/`):** Clean, responsive portal for inputting student details, resume content, and target job descriptions.
- **Weighted ATS Scoring Engine (`/analyze`):** Deterministic Python NLP algorithm evaluating Keyword Match (55%), Action Verbs (25%), and Structural Hygiene (20%).
- **Visual Optimization Scorecard (`result.html`):** Pure CSS circular progress ring, green matched skill badges, red missing keyword alerts, and formatting tips.
- **Placement Cell ERP Analytics (`/admin`):** Relational SQL database logging every student audit for department-wide readiness monitoring.

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3 (Responsive Grid, Pure CSS Conic-Gradient Gauge)
- **Backend:** Python 3, Flask
- **Database:** SQLite / MySQL Relational Schema

## 🚀 How to Run Locally
```bash
pip install flask
python app.py
```
Open `http://127.0.0.1:5050` in your browser.
