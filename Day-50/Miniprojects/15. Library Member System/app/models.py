from . import db
from datetime import date

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    join_date = db.Column(db.Date, default=date.today)

    def __repr__(self):
        return f"<Member {self.name}>"