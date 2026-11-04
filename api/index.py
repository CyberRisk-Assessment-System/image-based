from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3, os, uuid

app = Flask(__name__)
CORS(app)

VALID_IDS = {f"IMG_{i:02d}" for i in range(1, 13)}
DB_PATH = "/tmp/submissions.db"

def init_db():
    con = sqlite3.connect(DB_PATH)
    con.execute("""
        CREATE TABLE IF NOT EXISTS image_submissions (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id      TEXT,
            question_id     TEXT NOT NULL,
            selected_option TEXT NOT NULL,
            created_at      TEXT DEFAULT (datetime('now'))
        )
    """)
    con.commit()
    con.close()

try:
    init_db()
except Exception:
    pass

@app.route("/api/image-submissions", methods=["POST"])
def submit():
    try:
        data = request.get_json(force=True)
        session_id = data.get("session_id") or str(uuid.uuid4())
        answers = data.get("answers", [])

        for item in answers:
            qid = item.get("question_id", "")
            opt = item.get("selected_option", "")
            if qid not in VALID_IDS:
                return jsonify({"error": f"Unknown question_id: {qid}"}), 422
            if opt not in ("A", "B"):
                return jsonify({"error": f"Invalid selected_option: {opt}"}), 422

        con = sqlite3.connect(DB_PATH)
        for item in answers:
            con.execute(
                "INSERT INTO image_submissions (session_id, question_id, selected_option) VALUES (?,?,?)",
                (session_id, item["question_id"], item["selected_option"])
            )
        con.commit()
        con.close()
        return jsonify({"status": "ok", "saved": len(answers), "session_id": session_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "CyberRisk Image Assessment API"}), 200
