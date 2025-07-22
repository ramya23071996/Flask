from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Expense
from .forms import ExpenseForm
from sqlalchemy import func

def register_routes(app):

    @app.route("/")
    def index():
        group_by = request.args.get("group_by")
        if group_by == "category":
            grouped = db.session.query(
                Expense.category,
                func.sum(Expense.amount)
            ).group_by(Expense.category).all()
            return render_template("expenses.html", grouped=grouped, mode="category")
        elif group_by == "date":
            grouped = db.session.query(
                Expense.date,
                func.sum(Expense.amount)
            ).group_by(Expense.date).order_by(Expense.date.desc()).all()
            return render_template("expenses.html", grouped=grouped, mode="date")
        else:
            expenses = Expense.query.order_by(Expense.date.desc()).all()
            return render_template("expenses.html", expenses=expenses, mode="list")

    @app.route("/add", methods=["GET", "POST"])
    def add_expense():
        form = ExpenseForm()
        if form.validate_on_submit():
            exp = Expense(
                name=form.name.data,
                amount=form.amount.data,
                category=form.category.data,
                date=form.date.data
            )
            db.session.add(exp)
            db.session.commit()
            flash("Expense added!", "success")
            return redirect("/")
        return render_template("expense_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_expense(id):
        exp = Expense.query.get_or_404(id)
        form = ExpenseForm(obj=exp)
        if form.validate_on_submit():
            exp.name = form.name.data
            exp.amount = form.amount.data
            exp.category = form.category.data
            exp.date = form.date.data
            db.session.commit()
            flash("Expense updated!", "success")
            return redirect("/")
        return render_template("expense_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_expense(id):
        exp = Expense.query.get_or_404(id)
        db.session.delete(exp)
        db.session.commit()
        flash("Expense deleted.", "info")
        return redirect("/")