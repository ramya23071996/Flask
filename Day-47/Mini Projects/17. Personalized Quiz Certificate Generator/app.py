from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory certificate log
certificates = []

# 1. /quiz-form – form to enter name and score
@app.route('/quiz-form', methods=['GET'])
def quiz_form():
    return '''
    <h2>Generate Your Quiz Certificate</h2>
    <form method="POST" action="/generate-certificate">
        Name: <input type="text" name="name"><br>
        Score: <input type="number" name="score" min="0" max="10"><br>
        <input type="submit" value="Generate Certificate">
    </form>
    '''

# 2. /generate-certificate – handle POST and redirect
@app.route('/generate-certificate', methods=['POST'])
def generate_certificate():
    name = request.form.get('name', 'Anonymous').strip()
    score = request.form.get('score', '0').strip()

    # Store certificate
    certificates.append({
        'name': name,
        'score': int(score)
    })

    # Redirect to personalized certificate
    return redirect(url_for('certificate', name=name, score=score))

# 3. /certificate/<name>/<score> – dynamic certificate view
@app.route('/certificate/<name>/<int:score>')
def certificate(name, score):
    return f"""
    <h3>🎓 Certificate of Achievement</h3>
    <p>This certifies that <strong>{escape(name)}</strong> scored <strong>{score}/10</strong> on the quiz.</p>
    <p>Congratulations!</p>
    """

# 4. /certificates?score=10 – filter by score
@app.route('/certificates')
def certificates_by_score():
    score = request.args.get('score', '').strip()
    try:
        score = int(score)
    except ValueError:
        return "<p>Invalid score value.</p>"

    filtered = [c for c in certificates if c['score'] == score]
    if not filtered:
        return f"<p>No certificates found for score: {score}</p>"

    items = "".join([
        f"<li><a href='{url_for('certificate', name=c['name'], score=c['score'])}'>{escape(c['name'])} – {c['score']}/10</a></li>"
        for c in filtered
    ])
    return f"<h3>Certificates with Score {score}</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)