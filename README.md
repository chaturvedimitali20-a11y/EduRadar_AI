# EduRadar AI — Student Career Readiness & ATS Optimization Portal

**Competition:** PRASUNEX INNOVATHON 2026 (Round 3 Working Prototype)  
**Innovator:** Mitali Chaturvedi (Solo Participant)  

### 🎥 Prototype Demonstration Video
* **Watch Online (LinkedIn Post):** [View Live Prototype Walkthrough on LinkedIn](https://lnkd.in/p/guH4JKjX)
* **Direct Video File:** Download and play the `.mp4` demonstration video uploaded directly inside this repository.

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
1. Clone or download this repository and open the folder in **VS Code** (or **Command Prompt / Terminal**).
2. Open the terminal inside the project directory (`Ctrl + ~` in VS Code) and install Flask:
   ```bash
   pip install flask
   ```
3. Start the local Flask server:
   ```bash
   python app.py
   ```
4. Open **`http://127.0.0.1:5050`** in Google Chrome or any web browser.
