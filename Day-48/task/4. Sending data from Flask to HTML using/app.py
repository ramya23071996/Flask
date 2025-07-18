from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="Mahesh", title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, title="User Page")

@app.route('/courses')
def courses():
    return render_template('courses.html', courses=["Python", "Flask", "Jinja"], title="Courses")

@app.route('/profile')
def profile():
    user = {"name": "Mahesh", "age": 28, "city": "Coimbatore"}
    return render_template('profile.html', user=user, title="Profile")

@app.route('/datetime')
def show_datetime():
    return render_template('datetime.html', now=datetime.now(), title="Date & Time")

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', title="404"), 404

if __name__ == '__main__':
    app.run(debug=True)