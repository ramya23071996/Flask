from flask import render_template, request, redirect, flash, jsonify
from . import db
from .models import User, Product, Blog
from .forms import BlogForm

def register_routes(app):

    # 1. Create new user
    @app.route("/add_user", methods=["POST"])
    def add_user():
        try:
            user = User(name=request.form["name"], email=request.form["email"])
            db.session.add(user)  # Add to session
            db.session.commit()   # Commit changes
            flash("User created successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
        return redirect("/")

    # 2. Add product
    @app.route("/add_product", methods=["POST"])
    def add_product():
        product = Product(name="Mousepad", price=199.00)
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added"})

    # 3. Blog form creation
    @app.route("/new_blog", methods=["GET", "POST"])
    def new_blog():
        form = BlogForm()
        if form.validate_on_submit():
            blog = Blog(title=form.title.data, content=form.content.data)
            db.session.add(blog)
            db.session.commit()
            flash("Blog posted!", "success")
            return redirect("/new_blog")
        return render_template("add_blog.html", form=form)

    # 4. Dummy records
    @app.route("/seed_data")
    def seed_data():
        dummy_users = [
            User(name=f"User{i}", email=f"user{i}@test.com") for i in range(5)
        ]
        db.session.bulk_save_objects(dummy_users)
        db.session.commit()
        return jsonify({"message": "Dummy users added"})

    # 5. Bulk insert products
    @app.route("/bulk_products")
    def bulk_products():
        items = [
            Product(name=f"Item{i}", price=99 + i) for i in range(5)
        ]
        db.session.bulk_save_objects(items)
        db.session.commit()
        return jsonify({"message": "Products inserted"})