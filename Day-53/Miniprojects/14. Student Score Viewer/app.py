from flask import Flask, jsonify, render_template

app = Flask(__name__)

students = [
    {"id": 1, "name": "Arjun"},
    {"id": 2, "name": "Lakshmi"},
    {"id": 3, "name": "Ravi"}
]

scores = {
    1: {"Math": 89, "Science": 92, "English": 85},
    2: {"Math": 76, "Science": 80, "English": 78},
    3: {"Math": 91, "Science": 88, "English": 90}
}

@app.route('/')
def index():
    return render_template('students.html', students=students)

@app.route('/api/score/<int:student_id>')
def get_score(student_id):
    data = scores.get(student_id)
    if data:
        return jsonify(data)
    return jsonify({"error": "Student not found"}), 404