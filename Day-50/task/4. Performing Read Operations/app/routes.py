from flask import render_template, jsonify
from .models import User, Product, Blog

def register_routes(app):
    
    # 1. All users
    @app.route("/users")
    def all_users():
        users = User.query.all()
        return render_template("users.html", users=users)

    # 2. User by ID
    @app.route("/user/<int:id>")
    def get_user(id):
        user = User.query.get(id)
        if user:
            return render_template("user_details.html", user=user)
        return "User not found", 404

    # 3. Filter by email
    @app.route("/find_user/<email>")
    def find_user(email):
        user = User.query.filter_by(email=email).first()
        return jsonify({"name": user.name}) if user else "No match"

    # 4. In-stock products
    @app.route("/products/available")
    def in_stock():
        products = Product.query.filter_by(in_stock=True).all()
        return jsonify([p.name for p in products])

    # 5. Blogs ordered by date DESC
    @app.route("/blogs")
    def latest_blogs():
        blogs = Blog.query.order_by(Blog.created_at.desc()).all()
        return render_template("blogs.html", blogs=blogs)

    # 6. Count users
    @app.route("/user_count")
    def user_count():
        total = User.query.count()
        return jsonify({"total_users": total})

    # 10. Dict conversion
    @app.route("/debug_user/<int:id>")
    def user_dict(id):
        user = User.query.get(id)
        if user:
            user_dict = {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
            print(user_dict)  # Log
            return user_dict
        return "User not found"