from flask import render_template, redirect, url_for, flash, request
from datetime import datetime
from . import db
from .models import Appointment
from .forms import AppointmentForm

def register_routes(app):

    @app.route("/")
    def index():
        appointments = Appointment.query.order_by(Appointment.date, Appointment.time).all()
        return render_template("appointments.html", appointments=appointments)

    @app.route("/book", methods=["GET", "POST"])
    def book():
        form = AppointmentForm()
        if form.validate_on_submit():
            appt = Appointment(
                name=form.name.data,
                date=form.date.data,
                time=form.time.data,
                status=form.status.data
            )
            db.session.add(appt)
            db.session.commit()
            flash("Appointment booked!", "success")
            return redirect("/")
        return render_template("appointment_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit(id):
        appt = Appointment.query.get_or_404(id)
        form = AppointmentForm(obj=appt)
        if form.validate_on_submit():
            appt.name = form.name.data
            appt.date = form.date.data
            appt.time = form.time.data
            appt.status = form.status.data
            db.session.commit()
            flash("Appointment updated!", "success")
            return redirect("/")
        return render_template("appointment_form.html", form=form)

    @app.route("/delete_expired")
    def delete_expired():
        today = datetime.today().date()
        expired = Appointment.query.filter(Appointment.date < today).all()
        for appt in expired:
            db.session.delete(appt)
        db.session.commit()
        flash("Expired appointments deleted.", "info")
        return redirect("/")