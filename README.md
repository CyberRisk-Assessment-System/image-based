# CyberRisk — Image-Based Questionnaire

A visual, forced-choice cybersecurity risk assessment questionnaire based on personality traits and risk behaviours.

## Features
- **12 Image-Based Forced-Choice Items** (Conscientiousness, Agreeableness, Extraversion, Openness, Neuroticism).
- **Interactive UI**: Clean, responsive interface served directly via Flask.
- **Backend API & Database**: Python Flask backend storing submissions in SQLite (`submissions.db`).
- **Scoring & Profiling**: Immediate risk scoring and profile summary upon test completion.

## Project Structure
```text
.
├── app.py              # Flask server and API endpoints
├── index.html          # Questionnaire UI and scoring logic
├── images/             # 24 visual choice image cards (q1a.png – q12b.png)
├── submissions.db      # SQLite database for answers
└── requirements.txt    # Python dependencies
```

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser at:
   ```
   http://127.0.0.1:5000/
   ```
