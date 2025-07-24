from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100))
    status = db.Column(db.String(20))  # e.g., "Yes", "No", "Maybe"
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def update_status(self, new_status):
        self.status = new_status