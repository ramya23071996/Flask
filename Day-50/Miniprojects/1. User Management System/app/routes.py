from flask import render_template, redirect, flash, request, url_for
from . import db
from .models import User
from .forms import UserForm

def register_routes(app):
    @app.route("/")
    def list_users():
        users = User.query.all()
        return render_template("users.html", users=users)

    @app.route("/add", methods=["GET", "POST"])
    def add_user():
        form = UserForm()
        if form.validate_on_submit():
            try:
                user = User(
                    name=form.name.data,
                    email=form.email.data,
                    password=form.password.data
                )
                db.session.add(user)
                db.session.commit()
                flash("User added!", "success")
                return redirect("/")
            except Exception as e:
                db.session.rollback()
                flash(f"Error: {str(e)}", "danger")
        return render_template("user_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_user(id):
        user = User.query.get_or_404(id)
        form = UserForm(obj=user)
        if form.validate_on_submit():
            user.name = form.name.data
            user.email = form.email.data
            user.password = form.password.data
            db.session.commit()
            flash("User updated!", "success")
            return redirect("/")
        return render_template("user_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_user(id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        flash("User deleted!", "info")
        return redirect("/")