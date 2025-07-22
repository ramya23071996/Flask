from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Boolean, default=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Product {self.name} ₹{self.price}>"