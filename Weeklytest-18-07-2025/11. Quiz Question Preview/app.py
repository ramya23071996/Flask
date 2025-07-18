from flask import Flask, render_template

app = Flask(__name__)

# Simulated quiz question bank
quiz_data = {
    "1": {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "Rome"]
    },
    "2": {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"]
    },
    "3": {
        "question": "Which language is used for web apps?",
        "options": ["Python", "HTML", "JavaScript", "All of the above"]
    }
}

@app.route('/quiz/<question_id>')
def quiz(question_id):
    question = quiz_data.get(question_id)
    if not question:
        return f"<h2>Question ID {question_id} not found.</h2>"

    return render_template('quiz.html', question=question, question_id=question_id)

if __name__ == '__main__':
    app.run(debug=True)
