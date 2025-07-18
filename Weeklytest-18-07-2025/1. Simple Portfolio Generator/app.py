from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    skills = request.form['skills']
    bio = request.form['bio']
    return redirect(url_for('profile', name=name, skills=skills, bio=bio))

@app.route('/profile/<name>')
def profile(name):
    skills = request.args.get('skills')
    bio = request.args.get('bio')
    return render_template('profile.html', name=name, skills=skills, bio=bio)

if __name__ == '__main__':
    app.run(debug=True)