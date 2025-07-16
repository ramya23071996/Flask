from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# 1. /start → redirects to /home
@app.route('/start')
def start():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return "<h2>Welcome to the Home Page!</h2>"

# 2. /dashboard → redirects to /login if not 'logged in'
@app.route('/dashboard')
def dashboard():
    logged_in = request.args.get('logged_in', 'false')  # Simulated login check
    if logged_in != 'true':
        return redirect(url_for('login'))
    return "<h2>Dashboard: You are logged in!</h2>"

@app.route('/login')
def login():
    return '''
    <form method="POST" action="/do-login">
        Username: <input type="text" name="username"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/do-login', methods=['POST'])
def do_login():
    username = request.form.get('username', 'Guest')
    return redirect(url_for('thankyou', name=username))

# 3. /profile/<username> – dynamic link generation
@app.route('/profile/<username>')
def profile(username):
    return f"<h2>Welcome, {escape(username)}!</h2>"

# 4. /links – HTML links using url_for()
@app.route('/links')
def links():
    home_link = url_for('home')
    profile_link = url_for('profile', username='mahesh')
    dashboard_link = url_for('dashboard')
    return f"""
    <h3>Navigation</h3>
    <ul>
        <li><a href="{home_link}">Home</a></li>
        <li><a href="{profile_link}">Mahesh's Profile</a></li>
        <li><a href="{dashboard_link}">Dashboard</a></li>
    </ul>
    """

# 5. /thankyou – used after form submission
@app.route('/thankyou')
def thankyou():
    name = request.args.get('name', 'Guest')
    return f"<h2>Thank you, {escape(name)}!</h2>"

if __name__ == '__main__':
    app.run(debug=True)