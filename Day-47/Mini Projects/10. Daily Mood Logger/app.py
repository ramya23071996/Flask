from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory mood log
mood_logs = []

# 1. /log-mood – form to log mood
@app.route('/log-mood', methods=['GET'])
def log_mood():
    return '''
    <h2>Log Your Mood</h2>
    <form method="POST" action="/mood-result">
        Name: <input type="text" name="name"><br>
        Mood:
        <select name="mood">
            <option value="happy">Happy</option>
            <option value="sad">Sad</option>
            <option value="angry">Angry</option>
            <option value="excited">Excited</option>
        </select><br>
        Reason: <textarea name="reason"></textarea><br>
        <input type="submit" value="Log Mood">
    </form>
    '''

# 2. /mood-result – handle POST and redirect
@app.route('/mood-result', methods=['POST'])
def mood_result():
    name = request.form.get('name', '').strip()
    mood = request.form.get('mood', '').strip().lower()
    reason = request.form.get('reason', '').strip()

    # Save mood log
    mood_logs.append({
        'name': name,
        'mood': mood,
        'reason': reason
    })

    # Redirect to thank-you page
    return redirect(url_for('thank_you_mood', name=name))

# 3. /thank-you/<name> – dynamic thank-you message
@app.route('/thank-you/<name>')
def thank_you_mood(name):
    return f"<h3>Thank you, {escape(name)}! Your mood has been logged.</h3>"

# 4. /logs?mood=happy – filter mood entries
@app.route('/logs')
def mood_logs_view():
    mood = request.args.get('mood', '').strip().lower()
    filtered = [m for m in mood_logs if m['mood'] == mood] if mood else mood_logs

    if not filtered:
        return f"<p>No mood logs found for mood: {escape(mood)}</p>"

    items = "".join([
        f"<li>{escape(m['name'])} felt <strong>{escape(m['mood'])}</strong> – {escape(m['reason'])}</li>"
        for m in filtered
    ])
    return f"<h3>Mood Logs</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)