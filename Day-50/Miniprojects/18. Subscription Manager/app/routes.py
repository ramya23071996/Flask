from flask import render_template, redirect, url_for, flash
from . import db
from .models import Subscriber
from .forms import SubscriberForm

def register_routes(app):

    @app.route("/")
    def index():
        subscribers = Subscriber.query.order_by(Subscriber.subscribed_on.desc()).all()
        return render_template("subscribers.html", subscribers=subscribers)

    @app.route("/add", methods=["GET", "POST"])
    def add():
        form = SubscriberForm()
        if form.validate_on_submit():
            s = Subscriber(
                email=form.email.data,
                plan=form.plan.data,
                subscribed_on=form.subscribed_on.data
            )
            db.session.add(s)
            db.session.commit()
            flash("Subscriber added!", "success")
            return redirect("/")
        return render_template("subscriber_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit(id):
        s = Subscriber.query.get_or_404(id)
        form = SubscriberForm(obj=s)
        if form.validate_on_submit():
            s.email = form.email.data
            s.plan = form.plan.data
            s.subscribed_on = form.subscribed_on.data
            db.session.commit()
            flash("Subscription updated!", "success")
            return redirect("/")
        return render_template("subscriber_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete(id):
        s = Subscriber.query.get_or_404(id)
        db.session.delete(s)
        db.session.commit()
        flash("Subscriber deleted.", "info")
        return redirect("/")