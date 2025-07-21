from flask import Flask, render_template, flash
from forms import PasswordResetForm

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/reset", methods=["GET", "POST"])
def reset_password():
    form = PasswordResetForm()
    if form.validate_on_submit():
        flash("Your password has been reset successfully!", "success")
    return render_template("reset.html", form=form)
