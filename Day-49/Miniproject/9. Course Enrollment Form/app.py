from flask import Flask, render_template, flash
from forms import EnrollmentForm

app = Flask(__name__)
app.secret_key = "enrollmentsecretkey"

@app.route("/enroll", methods=["GET", "POST"])
def enroll():
    form = EnrollmentForm()
    if form.validate_on_submit():
        flash(f"Hi {form.student_name.data}, you enrolled in {form.course.choices[form.course.data == form.course.choices[0][0] and 0 or 1][1]}!", "success")
        return render_template("enroll.html", form=form)
    return render_template("enroll.html", form=form)
