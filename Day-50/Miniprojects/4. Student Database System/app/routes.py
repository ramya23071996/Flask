from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Student
from .forms import StudentForm

def register_routes(app):

    @app.route("/")
    def index():
        students = Student.query.order_by(Student.id.desc()).all()
        return render_template("students.html", students=students)

    @app.route("/register", methods=["GET", "POST"])
    def register_student():
        form = StudentForm()
        if form.validate_on_submit():
            student = Student(
                name=form.name.data,
                roll_no=form.roll_no.data,
                email=form.email.data,
                age=form.age.data
            )
            db.session.add(student)
            db.session.commit()
            flash("Student registered successfully!", "success")
            return redirect("/")
        return render_template("student_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_student(id):
        student = Student.query.get_or_404(id)
        form = StudentForm(obj=student)
        if form.validate_on_submit():
            student.name = form.name.data
            student.roll_no = form.roll_no.data
            student.email = form.email.data
            student.age = form.age.data
            db.session.commit()
            flash("Student updated!", "success")
            return redirect("/")
        return render_template("student_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_student(id):
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        flash("Student deleted!", "info")
        return redirect("/")