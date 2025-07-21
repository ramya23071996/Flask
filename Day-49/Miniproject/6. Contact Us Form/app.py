from flask import Flask, render_template, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = "contactussecret"

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # You could add logic to store or send the message here
        flash(f"Thank you, {form.name.data}! Your message has been sent.", "success")
        return render_template("contact.html", form=form)

    return render_template("contact.html", form=form)
