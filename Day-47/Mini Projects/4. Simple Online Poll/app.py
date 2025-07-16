from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory vote store
votes = []  # Each vote is {'name': ..., 'option': ...}

# 1. /poll – show voting form
@app.route('/poll', methods=['GET'])
def poll():
    return '''
    <h2>Vote for Your Favorite Option</h2>
    <form method="POST" action="/vote">
        Name: <input type="text" name="name"><br>
        Choose an option:
        <select name="option">
            <option value="A">Option A</option>
            <option value="B">Option B</option>
            <option value="C">Option C</option>
        </select><br>
        <input type="submit" value="Vote">
    </form>
    '''

# 2. /vote – handle vote and redirect
@app.route('/vote', methods=['POST'])
def vote():
    name = request.form.get('name', '').strip()
    option = request.form.get('option', '').strip().upper()

    # Store vote
    votes.append({
        'name': name,
        'option': option
    })

    # Redirect to result page with selected option
    return redirect(url_for('result', option=option))

# 3. /result?option=A – show vote count for option
@app.route('/result')
def result():
    option = request.args.get('option', '').strip().upper()
    count = sum(1 for v in votes if v['option'] == option)

    return f"<h3>Votes for Option {escape(option)}: {count}</h3>"

# 4. /voter/<name> – show user's selected vote
@app.route('/voter/<name>')
def voter(name):
    match = next((v for v in votes if v['name'].lower() == name.lower()), None)
    if match:
        return f"<h3>{escape(name)} voted for Option {escape(match['option'])}</h3>"
    return f"<p>No vote found for {escape(name)}</p>"

if __name__ == '__main__':
    app.run(debug=True)