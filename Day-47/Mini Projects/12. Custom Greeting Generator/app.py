from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# 1. /greet – query-based greeting
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest').strip()
    time = request.args.get('time', 'day').strip().lower()

    greeting = {
        'morning': 'Good morning',
        'afternoon': 'Good afternoon',
        'evening': 'Good evening',
        'night': 'Good night'
    }.get(time, 'Hello')

    return f"<h3>{greeting}, {escape(name)}!</h3>"

# 2. /custom-greet/<name> – dynamic route greeting
@app.route('/custom-greet/<name>')
def custom_greet(name):
    return f"<h3>Hello, {escape(name)}! Hope you're having a great day!</h3>"

# 3. /submit-greet – form to enter name and time
@app.route('/submit-greet', methods=['GET', 'POST'])
def submit_greet():
    if request.method == 'POST':
        name = request.form.get('name', 'Guest').strip()
        time = request.form.get('time', 'day').strip().lower()
        return redirect(url_for('greet_result', name=name, time=time))

    return '''
    <h2>Generate Your Greeting</h2>
    <form method="POST">
        Name: <input type="text" name="name"><br>
        Time of Day:
        <select name="time">
            <option value="morning">Morning</option>
            <option value="afternoon">Afternoon</option>
            <option value="evening">Evening</option>
            <option value="night">Night</option>
        </select><br>
        <input type="submit" value="Get Greeting">
    </form>
    '''

# 4. /greet-result – final greeting after form submission
@app.route('/greet-result')
def greet_result():
    name = request.args.get('name', 'Guest').strip()
    time = request.args.get('time', 'day').strip().lower()

    greeting = {
        'morning': 'Good morning',
        'afternoon': 'Good afternoon',
        'evening': 'Good evening',
        'night': 'Good night'
    }.get(time, 'Hello')

    return f"<h3>{greeting}, {escape(name)}! Your greeting has been generated.</h3>"

if __name__ == '__main__':
    app.run(debug=True)