from flask import render_template, redirect, url_for, flash
from . import db
from .models import Complaint
from .forms import ComplaintForm

def register_routes(app):

    @app.route("/")
    def index():
        complaints = Complaint.query.order_by(Complaint.id.desc()).all()
        total = len(complaints)
        resolved = len([c for c in complaints if c.resolved])
        return render_template("complaints.html", complaints=complaints, total=total, resolved=resolved)

    @app.route("/submit", methods=["GET", "POST"])
    def submit():
        form = ComplaintForm()
        if form.validate_on_submit():
            c = Complaint(name=form.name.data, message=form.message.data)
            db.session.add(c)
            db.session.commit()
            flash("Complaint submitted!", "success")
            return redirect("/")
        return render_template("complaint_form.html", form=form)

    @app.route("/resolve/<int:id>", methods=["GET", "POST"])
    def resolve(id):
        c = Complaint.query.get_or_404(id)
        form = ComplaintForm(obj=c)
        if form.validate_on_submit():
            c.resolved = form.resolved.data
            db.session.commit()
            flash("Complaint status updated!", "success")
            return redirect("/")
        return render_template("complaint_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete(id):
        c = Complaint.query.get_or_404(id)
        db.session.delete(c)
        db.session.commit()
        flash("Complaint deleted.", "info")
        return redirect("/")