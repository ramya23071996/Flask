from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Employee
from .forms import EmployeeForm

def register_routes(app):

    @app.route("/")
    def index():
        dept_filter = request.args.get("department")
        if dept_filter:
            employees = Employee.query.filter_by(department=dept_filter).all()
        else:
            employees = Employee.query.order_by(Employee.id.desc()).all()
        return render_template("employees.html", employees=employees, dept_filter=dept_filter)

    @app.route("/add", methods=["GET", "POST"])
    def add_employee():
        form = EmployeeForm()
        if form.validate_on_submit():
            emp = Employee(
                name=form.name.data,
                position=form.position.data,
                department=form.department.data,
                salary=form.salary.data
            )
            db.session.add(emp)
            db.session.commit()
            flash("Employee added!", "success")
            return redirect("/")
        return render_template("employee_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_employee(id):
        emp = Employee.query.get_or_404(id)
        form = EmployeeForm(obj=emp)
        if form.validate_on_submit():
            emp.name = form.name.data
            emp.position = form.position.data
            emp.department = form.department.data
            emp.salary = form.salary.data
            db.session.commit()
            flash("Employee updated!", "success")
            return redirect("/")
        return render_template("employee_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_employee(id):
        emp = Employee.query.get_or_404(id)
        db.session.delete(emp)
        db.session.commit()
        flash("Employee deleted.", "info")
        return redirect("/")