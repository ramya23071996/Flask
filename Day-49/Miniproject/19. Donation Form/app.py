from flask import Flask, render_template, flash
from forms import DonationForm

app = Flask(__name__)
app.secret_key = 'donate123'

@app.route("/donate", methods=["GET", "POST"])
def donate():
    form = DonationForm()
    if form.validate_on_submit():
        amount = form.amount.data
        cause = form.cause.data
        flash(f"Thank you for donating ₹{amount} to {cause.capitalize()}!", "success")
    return render_template("donation.html", form=form)
