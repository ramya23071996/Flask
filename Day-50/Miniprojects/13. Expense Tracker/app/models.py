from . import db
from datetime import date

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, default=date.today)

    def __repr__(self):
        return f"<Expense {self.name}: ₹{self.amount} ({self.category})>"