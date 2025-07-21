from flask import Flask, render_template, flash
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'dummyloginkey'

# Dummy credentials
DUMMY_EMAIL = 'user@example.com'
DUMMY_PASSWORD = 'secret123'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == DUMMY_EMAIL and form.password.data == DUMMY_PASSWORD:
            flash("Login successful", "success")
        else:
            flash("Invalid credentials", "error")
    return render_template('login.html', form=form)
