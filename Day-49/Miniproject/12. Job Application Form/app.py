from flask import Flask, render_template, flash
from forms import JobApplicationForm

app = Flask(__name__)
app.secret_key = "jobappsecret"

@app.route("/apply", methods=["GET", "POST"])
def apply():
    form = JobApplicationForm()
    if form.validate_on_submit():
        flash(f"Thank you {form.name.data}, your application has been received!", "success")
    return render_template("job_application.html", form=form)
