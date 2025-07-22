from . import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="Applied")  # Applied / Shortlisted / Rejected

    def __repr__(self):
        return f"<Application {self.name} - {self.job_title}>"