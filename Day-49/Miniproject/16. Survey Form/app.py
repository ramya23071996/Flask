from flask import Flask, render_template, flash
from forms import SurveyForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route("/survey", methods=["GET", "POST"])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        flash("Thanks for participating!", "success")
    return render_template("survey.html", form=form)
