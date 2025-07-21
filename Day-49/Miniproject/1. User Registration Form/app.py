from flask import Flask, render_template, flash
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Welcome, {form.full_name.data}! Registration successful.", "success")
        return render_template("register.html", form=form)

    return render_template("register.html", form=form)
