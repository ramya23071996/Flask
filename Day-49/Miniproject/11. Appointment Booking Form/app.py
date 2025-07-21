from flask import Flask, render_template, flash
from forms import AppointmentForm

app = Flask(__name__)
app.secret_key = "appointmentsecret"

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        flash(f"Appointment confirmed on {form.date.data.strftime('%Y-%m-%d')} at {form.time.data.strftime('%H:%M')}", "success")
        return render_template("appointment.html", form=form)
    return render_template("appointment.html", form=form)
