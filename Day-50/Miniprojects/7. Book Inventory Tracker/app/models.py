from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    published_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Book {self.title} ({self.published_year})>"