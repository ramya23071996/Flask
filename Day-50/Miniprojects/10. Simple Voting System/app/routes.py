from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Candidate, Vote
from .forms import VoteForm

def register_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def vote():
        form = VoteForm()
        form.candidate_id.choices = [(c.id, f"{c.name} ({c.party})") for c in Candidate.query.all()]

        if form.validate_on_submit():
            if Vote.query.filter_by(voter_name=form.voter_name.data).first():
                flash("Duplicate vote detected!", "danger")
            else:
                vote = Vote(voter_name=form.voter_name.data, candidate_id=form.candidate_id.data)
                db.session.add(vote)
                db.session.commit()
                flash("Vote cast successfully!", "success")
            return redirect("/")

        return render_template("vote.html", form=form)

    @app.route("/results")
    def results():
        candidates = Candidate.query.all()
        counts = {c.name: len(c.votes) for c in candidates}
        return render_template("results.html", counts=counts)