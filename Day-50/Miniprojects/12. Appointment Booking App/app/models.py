from . import db
from datetime import date, time

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), default="Pending")  # Confirmed / Canceled

    def __repr__(self):
        return f"<Appointment {self.name} on {self.date} at {self.time}>"