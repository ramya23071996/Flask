from flask import render_template, redirect, url_for, flash
from . import db
from .models import Member
from .forms import MemberForm

def register_routes(app):

    @app.route("/")
    def index():
        members = Member.query.order_by(Member.join_date.asc()).all()
        return render_template("members.html", members=members)

    @app.route("/add", methods=["GET", "POST"])
    def add_member():
        form = MemberForm()
        if form.validate_on_submit():
            m = Member(
                name=form.name.data,
                email=form.email.data,
                join_date=form.join_date.data
            )
            db.session.add(m)
            db.session.commit()
            flash("Member added!", "success")
            return redirect("/")
        return render_template("member_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_member(id):
        m = Member.query.get_or_404(id)
        db.session.delete(m)
        db.session.commit()
        flash("Member deleted.", "info")
        return redirect("/")