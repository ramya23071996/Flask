from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory quiz results
quiz_results = []

# Sample correct answers for scoring
correct_answers = {
    'q1': 'A',
    'q2': 'B',
    'q3': 'C'
}

# 1. /quiz – form with name and 3 MCQs
@app.route('/quiz', methods=['GET'])
def quiz():
    return '''
    <h2>Student Quiz</h2>
    <form method="POST" action="/quiz-result">
        Name: <input type="text" name="name"><br><br>

        1. What is 2 + 2?<br>
        <input type="radio" name="q1" value="A"> 4<br>
        <input type="radio" name="q1" value="B"> 3<br>
        <input type="radio" name="q1" value="C"> 5<br><br>

        2. What is the capital of France?<br>
        <input type="radio" name="q2" value="A"> Berlin<br>
        <input type="radio" name="q2" value="B"> Paris<br>
        <input type="radio" name="q2" value="C"> Rome<br><br>

        3. Which language is used for web styling?<br>
        <input type="radio" name="q3" value="A"> HTML<br>
        <input type="radio" name="q3" value="B"> Python<br>
        <input type="radio" name="q3" value="C"> CSS<br><br>

        <input type="submit" value="Submit Quiz">
    </form>
    '''

# 2. /quiz-result – handle POST and redirect
@app.route('/quiz-result', methods=['POST'])
def quiz_result():
    name = request.form.get('name', '').strip()
    answers = {
        'q1': request.form.get('q1', ''),
        'q2': request.form.get('q2', ''),
        'q3': request.form.get('q3', '')
    }

    # Calculate score
    score = sum(1 for q, a in answers.items() if correct_answers.get(q) == a)

    # Store result
    quiz_results.append({
        'name': name,
        'answers': answers,
        'score': score
    })

    # Redirect to summary page
    return redirect(url_for('quiz_summary', name=name))

# 3. /quiz-summary/<name> – show answers and score
@app.route('/quiz-summary/<name>')
def quiz_summary(name):
    match = next((r for r in quiz_results if r['name'].lower() == name.lower()), None)
    if not match:
        return f"<p>No quiz result found for {escape(name)}</p>"

    answers_html = "".join([
        f"<li>Q{i[-1]}: {escape(ans)} {'✅' if correct_answers[i] == ans else '❌'}</li>"
        for i, ans in match['answers'].items()
    ])
    return f"""
    <h3>Quiz Summary for {escape(match['name'])}</h3>
    <ul>{answers_html}</ul>
    <p><strong>Score:</strong> {match['score']} / 3</p>
    """

# 4. /leaderboard?score=3 – filter by score
@app.route('/leaderboard')
def leaderboard():
    score = request.args.get('score', '').strip()
    try:
        score = int(score)
    except ValueError:
        return "<p>Invalid score value.</p>"

    filtered = [r for r in quiz_results if r['score'] == score]
    if not filtered:
        return f"<p>No students found with score: {score}</p>"

    items = "".join([
        f"<li>{escape(r['name'])} – Score: {r['score']}</li>"
        for r in filtered
    ])
    return f"<h3>Leaderboard – Score {score}</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)