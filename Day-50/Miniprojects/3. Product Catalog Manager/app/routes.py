from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Product
from .forms import ProductForm

def register_routes(app):

    @app.route("/")
    def index():
        products = Product.query.order_by(Product.id.desc()).all()
        return render_template("products.html", products=products)

    @app.route("/add", methods=["GET", "POST"])
    def add_product():
        form = ProductForm()
        if form.validate_on_submit():
            product = Product(
                name=form.name.data,
                price=form.price.data,
                in_stock=form.in_stock.data,
                description=form.description.data
            )
            db.session.add(product)
            db.session.commit()
            flash("Product added!", "success")
            return redirect("/")
        return render_template("product_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_product(id):
        product = Product.query.get_or_404(id)
        form = ProductForm(obj=product)
        if form.validate_on_submit():
            product.name = form.name.data
            product.price = form.price.data
            product.in_stock = form.in_stock.data
            product.description = form.description.data
            db.session.commit()
            flash("Product updated!", "success")
            return redirect("/")
        return render_template("product_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_product(id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        flash("Product deleted!", "info")
        return redirect("/")

    @app.route("/available")
    def available_products():
        products = Product.query.filter_by(in_stock=True).all()
        return render_template("products.html", products=products)