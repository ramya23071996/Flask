from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Application
from .forms import ApplicationForm

def register_routes(app):

    @app.route("/")
    def index():
        status_filter = request.args.get("status")
        if status_filter:
            apps = Application.query.filter_by(status=status_filter).all()
        else:
            apps = Application.query.order_by(Application.id.desc()).all()
        return render_template("index.html", applications=apps, status_filter=status_filter)

    @app.route("/add", methods=["GET", "POST"])
    def add_application():
        form = ApplicationForm()
        if form.validate_on_submit():
            app_obj = Application(
                name=form.name.data,
                email=form.email.data,
                job_title=form.job_title.data,
                status=form.status.data
            )
            db.session.add(app_obj)
            db.session.commit()
            flash("Application added!", "success")
            return redirect("/")
        return render_template("application_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_application(id):
        app_obj = Application.query.get_or_404(id)
        form = ApplicationForm(obj=app_obj)
        if form.validate_on_submit():
            app_obj.name = form.name.data
            app_obj.email = form.email.data
            app_obj.job_title = form.job_title.data
            app_obj.status = form.status.data
            db.session.commit()
            flash("Application updated!", "success")
            return redirect("/")
        return render_template("application_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_application(id):
        app_obj = Application.query.get_or_404(id)
        db.session.delete(app_obj)
        db.session.commit()
        flash("Application deleted.", "info")
        return redirect("/")