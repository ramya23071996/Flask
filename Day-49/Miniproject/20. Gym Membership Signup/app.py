from flask import Flask, render_template, flash
from forms import GymSignupForm

app = Flask(__name__)
app.secret_key = "gym_secret"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = GymSignupForm()
    if form.validate_on_submit():
        flash(f"Welcome to our gym, {form.name.data}!", "success")
    return render_template("signup.html", form=form)
