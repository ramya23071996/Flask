from flask import render_template, redirect, url_for, flash
from . import db
from .models import Contact
from .forms import ContactForm

def register_routes(app):

    @app.route("/")
    def contact_list():
        contacts = Contact.query.order_by(Contact.name.asc()).all()
        return render_template("contacts.html", contacts=contacts)

    @app.route("/add", methods=["GET", "POST"])
    def add_contact():
        form = ContactForm()
        if form.validate_on_submit():
            contact = Contact(
                name=form.name.data,
                phone=form.phone.data,
                email=form.email.data,
                address=form.address.data
            )
            db.session.add(contact)
            db.session.commit()
            flash("Contact added!", "success")
            return redirect("/")
        return render_template("contact_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_contact(id):
        contact = Contact.query.get_or_404(id)
        form = ContactForm(obj=contact)
        if form.validate_on_submit():
            contact.name = form.name.data
            contact.phone = form.phone.data
            contact.email = form.email.data
            contact.address = form.address.data
            db.session.commit()
            flash("Contact updated!", "success")
            return redirect("/")
        return render_template("contact_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_contact(id):
        contact = Contact.query.get_or_404(id)
        db.session.delete(contact)
        db.session.commit()
        flash("Contact deleted!", "info")
        return redirect("/")