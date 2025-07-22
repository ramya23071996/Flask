from . import db

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    party = db.Column(db.String(100), nullable=False)
    votes = db.relationship('Vote', backref='candidate', lazy=True)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voter_name = db.Column(db.String(100), unique=True, nullable=False)  # prevent duplicates
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)

    def __repr__(self):
        return f"<Vote by {self.voter_name} for {self.candidate.name}>"