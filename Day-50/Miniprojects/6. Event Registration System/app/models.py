from . import db

class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    event_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Attendee {self.name} - {self.event_name}>"