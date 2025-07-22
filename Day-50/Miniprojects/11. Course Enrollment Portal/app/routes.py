from flask import render_template, redirect, url_for, flash
from . import db
from .models import Student, Course, Enrollment
from .forms import EnrollmentForm

def register_routes(app):

    @app.route("/")
    def view_enrollments():
        pairs = Enrollment.query.all()
        return render_template("enrollments.html", pairs=pairs)

    @app.route("/enroll", methods=["GET", "POST"])
    def enroll():
        form = EnrollmentForm()
        form.student_id.choices = [(s.id, s.name) for s in Student.query.all()]
        form.course_id.choices = [(c.id, c.name) for c in Course.query.all()]

        if form.validate_on_submit():
            enrollment = Enrollment(
                student_id=form.student_id.data,
                course_id=form.course_id.data
            )
            db.session.add(enrollment)
            db.session.commit()
            flash("Enrollment successful!", "success")
            return redirect("/")
        return render_template("enrollment_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_enrollment(id):
        enrollment = Enrollment.query.get_or_404(id)
        form = EnrollmentForm(obj=enrollment)
        form.student_id.choices = [(s.id, s.name) for s in Student.query.all()]
        form.course_id.choices = [(c.id, c.name) for c in Course.query.all()]

        if form.validate_on_submit():
            enrollment.student_id = form.student_id.data
            enrollment.course_id = form.course_id.data
            db.session.commit()
            flash("Enrollment updated!", "success")
            return redirect("/")
        return render_template("enrollment_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_enrollment(id):
        enrollment = Enrollment.query.get_or_404(id)
        db.session.delete(enrollment)
        db.session.commit()
        flash("Enrollment removed.", "info")
        return redirect("/")