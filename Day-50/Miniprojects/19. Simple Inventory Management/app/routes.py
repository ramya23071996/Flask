from flask import render_template, redirect, url_for, flash
from . import db
from .models import Item
from .forms import ItemForm

def register_routes(app):

    @app.route("/")
    def index():
        items = Item.query.order_by(Item.updated_on.desc()).all()
        return render_template("items.html", items=items)

    @app.route("/add", methods=["GET", "POST"])
    def add_item():
        form = ItemForm()
        if form.validate_on_submit():
            item = Item(name=form.name.data, quantity=form.quantity.data)
            db.session.add(item)
            db.session.commit()
            flash("Item added!", "success")
            return redirect("/")
        return render_template("item_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_item(id):
        item = Item.query.get_or_404(id)
        form = ItemForm(obj=item)
        if form.validate_on_submit():
            item.name = form.name.data
            item.quantity = form.quantity.data
            if item.quantity <= 0:
                db.session.delete(item)
                flash("Item removed due to zero stock.", "info")
            else:
                flash("Item updated!", "success")
            db.session.commit()
            return redirect("/")
        return render_template("item_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_item(id):
        item = Item.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        flash("Item deleted.", "info")
        return redirect("/")