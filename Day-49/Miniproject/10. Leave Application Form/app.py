from flask import Flask, render_template, flash
from forms import LeaveApplicationForm

app = Flask(__name__)
app.secret_key = "leavesecretkey"

@app.route("/leave", methods=["GET", "POST"])
def leave():
    form = LeaveApplicationForm()
    if form.validate_on_submit():
        days = (form.end_date.data - form.start_date.data).days + 1
        flash(f"Leave applied for {days} day(s).", "success")
        return render_template("leave.html", form=form)
    return render_template("leave.html", form=form)
