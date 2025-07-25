from flask import Flask, jsonify, render_template
import time

app = Flask(__name__)
QUIZ_DURATION = 120  # seconds
start_time = time.time()

questions = [
    {"id": 1, "question": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Chennai"]},
    {"id": 2, "question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Saturn"]},
]

@app.route('/')
def index():
    return render_template('quiz.html', questions=questions)

@app.route('/api/timer')
def timer():
    elapsed = time.time() - start_time
    remaining = max(QUIZ_DURATION - int(elapsed), 0)
    return jsonify({"remaining": remaining})