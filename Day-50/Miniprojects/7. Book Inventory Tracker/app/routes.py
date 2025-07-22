from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Book
from .forms import BookForm

def register_routes(app):

    @app.route("/")
    def book_list():
        books = Book.query.order_by(Book.published_year.asc()).all()
        return render_template("books.html", books=books)

    @app.route("/add", methods=["GET", "POST"])
    def add_book():
        form = BookForm()
        if form.validate_on_submit():
            book = Book(
                title=form.title.data,
                author=form.author.data,
                quantity=form.quantity.data,
                published_year=form.published_year.data
            )
            db.session.add(book)
            db.session.commit()
            flash("Book added to inventory!", "success")
            return redirect("/")
        return render_template("book_form.html", form=form)

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_book(id):
        book = Book.query.get_or_404(id)
        form = BookForm(obj=book)
        if form.validate_on_submit():
            book.title = form.title.data
            book.author = form.author.data
            book.quantity = form.quantity.data
            book.published_year = form.published_year.data
            db.session.commit()
            flash("Book updated!", "success")
            return redirect("/")
        return render_template("book_form.html", form=form)

    @app.route("/delete/<int:id>")
    def delete_book(id):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        flash("Book removed from inventory.", "info")
        return redirect("/")