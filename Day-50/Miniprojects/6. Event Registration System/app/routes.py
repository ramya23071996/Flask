from flask import render_template, redirect, url_for, flash
from . import db
from .models import Attendee
from .forms import AttendeeForm

def register_routes(app):

    @app.route("/")
    def attendee_list():
        attendees = Attendee.query.order_by(Attendee.id.desc()).all()
        return render_template("attendees.html", attendees=attendees)

    @app.route("/register", methods=["GET", "POST"])
    def register():
        form = AttendeeForm()
        if form.validate_on_submit():
            attendee = Attendee(
                name=form.name.data,
                email=form.email.data,
                event_name=form.event_name.data
            )
            db.session.add(attendee)
            db.session.commit()
            flash("Attendee registered!", "success")
            return redirect("/")
        return render_template("attendee_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_attendee(id):
        attendee = Attendee.query.get_or_404(id)
        form = AttendeeForm(obj=attendee)
        if form.validate_on_submit():
            attendee.name = form.name.data
            attendee.email = form.email.data
            attendee.event_name = form.event_name.data
            db.session.commit()
            flash("Attendee updated!", "success")
            return redirect("/")
        return render_template("attendee_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_attendee(id):
        attendee = Attendee.query.get_or_404(id)
        db.session.delete(attendee)
        db.session.commit()
        flash("Attendee removed.", "info")
        return redirect("/")