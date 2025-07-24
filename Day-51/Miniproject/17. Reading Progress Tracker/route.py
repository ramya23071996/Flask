from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, login_required, logout_user, current_user
from .models import db, User, Book
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('bp', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('bp.view_books'))
        flash('Invalid credentials')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    session.pop('last_viewed', None)
    return redirect(url_for('bp.login'))

@bp.route('/books')
@login_required
def view_books():
    books = Book.query.filter_by(user_id=current_user.id).all()
    last_viewed = session.get('last_viewed')
    return render_template('books.html', books=books, last_viewed=last_viewed)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_book():
    if request.method == 'POST':
        book = Book(
            title=request.form['title'],
            total_pages=int(request.form['total_pages']),
            pages_read=int(request.form['pages_read']),
            user_id=current_user.id
        )
        db.session.add(book)
        db.session.commit()
        session['last_viewed'] = book.title
        flash("Book added!")
        return redirect(url_for('bp.view_books'))
    return render_template('add_book.html')