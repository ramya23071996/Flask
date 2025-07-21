from flask import Flask, render_template, flash
from forms import ReviewForm

app = Flask(__name__)
app.secret_key = "reviewsecretkey"

@app.route("/review", methods=["GET", "POST"])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        flash(f"Thank you for your review, {form.name.data}!", "success")
        return render_template("review.html", form=form)
    return render_template("review.html", form=form)
