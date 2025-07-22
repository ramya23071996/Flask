from . import db
from datetime import datetime

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    plan = db.Column(db.String(50), nullable=False)
    subscribed_on = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Subscriber {self.email} - {self.plan}>"