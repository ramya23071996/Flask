from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory goal store
fitness_goals = []

# 1. /goal – form to submit fitness goal
@app.route('/goal', methods=['GET'])
def goal_form():
    return '''
    <h2>Set Your Fitness Goal</h2>
    <form method="POST" action="/goal-submit">
        Name: <input type="text" name="name"><br>
        Goal Type:
        <select name="type">
            <option value="weight">Weight Loss</option>
            <option value="muscle">Muscle Gain</option>
            <option value="cardio">Cardio Endurance</option>
        </select><br>
        <input type="submit" value="Submit Goal">
    </form>
    '''

# 2. /goal-submit – handle POST and redirect
@app.route('/goal-submit', methods=['POST'])
def goal_submit():
    name = request.form.get('name', 'Anonymous').strip()
    goal_type = request.form.get('type', 'general').strip().lower()

    # Store goal
    fitness_goals.append({
        'name': name,
        'type': goal_type
    })

    # Redirect to goal status page
    return redirect(url_for('goal_status', name=name))

# 3. /goal-status/<name> – personalized goal status
@app.route('/goal-status/<name>')
def goal_status(name):
    match = next((g for g in fitness_goals if g['name'].lower() == name.lower()), None)
    if match:
        return f"""
        <h3>Fitness Goal for {escape(match['name'])}</h3>
        <p>Goal Type: {escape(match['type'].capitalize())}</p>
        <p>Keep pushing toward your goal!</p>
        """
    return f"<p>No goal found for {escape(name)}</p>"

# 4. /goals?type=weight – filter goals by type
@app.route('/goals')
def goals_by_type():
    goal_type = request.args.get('type', '').strip().lower()
    filtered = [g for g in fitness_goals if g['type'] == goal_type] if goal_type else fitness_goals

    if not filtered:
        return f"<p>No goals found for type: {escape(goal_type)}</p>"

    items = "".join([
        f"<li>{escape(g['name'])} – Goal: {escape(g['type'].capitalize())}</li>"
        for g in filtered
    ])
    return f"<h3>Fitness Goals</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)