from flask import Flask, render_template, redirect, flash, get_flashed_messages, url_for
from forms import FlashForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FlashForm()

    if form.validate_on_submit():
        # Flash success message
        flash("Form submitted successfully!", "success")
        flash(f"Welcome, {form.name.data}!", "info")

        # Custom condition based on age
        if form.age.data > 60:
            flash("You're eligible for a senior discount!", "warning")

        # Dummy login success/failure check
        if form.email.data == "admin@example.com" and form.password.data == "admin123":
            flash("Login successful!", "success")
        else:
            flash("Login failed. Invalid credentials.", "error")

        # Flash warning if terms not accepted
        if not form.accept_terms.data:
            flash("You must accept the terms and conditions.", "warning")

        return redirect(url_for('index'))

    elif form.is_submitted():  # Form submitted but not valid
        # Specific flash for invalid email
        if form.email.errors:
            flash("Invalid email address!", "error")

        flash("Please correct the errors in the form.", "error")

    return render_template("form.html", form=form)
