from flask import request, jsonify
from . import db
from .models import User, Product, Blog

def register_routes(app):

    @app.route("/add_user", methods=["POST"])
    def add_user():
        data = request.json
        user = User(name=data["name"], email=data["email"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": f"User {user.name} created!"})
    
    @app.route("/products", methods=["GET"])
    def get_products():
        products = Product.query.filter_by(in_stock=True).all()
        return jsonify([p.name for p in products])