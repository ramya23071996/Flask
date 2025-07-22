from flask import render_template, redirect, url_for, flash
from . import db
from .models import Feedback
from .forms import FeedbackForm

def register_routes(app):

    @app.route("/")
    def index():
        feedbacks = Feedback.query.order_by(Feedback.id.desc()).all()
        return render_template("feedback.html", feedbacks=feedbacks)

    @app.route("/submit", methods=["GET", "POST"])
    def submit_feedback():
        form = FeedbackForm()
        if form.validate_on_submit():
            f = Feedback(
                user_name=form.user_name.data,
                rating=form.rating.data,
                comment=form.comment.data
            )
            db.session.add(f)
            db.session.commit()
            flash("Feedback submitted!", "success")
            return redirect("/")
        return render_template("feedback_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_feedback(id):
        f = Feedback.query.get_or_404(id)
        form = FeedbackForm(obj=f)
        if form.validate_on_submit():
            f.user_name = form.user_name.data
            f.rating = form.rating.data
            f.comment = form.comment.data
            db.session.commit()
            flash("Feedback updated!", "success")
            return redirect("/")
        return render_template("feedback_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_feedback(id):
        f = Feedback.query.get_or_404(id)
        db.session.delete(f)
        db.session.commit()
        flash("Feedback deleted.", "info")
        return redirect("/")