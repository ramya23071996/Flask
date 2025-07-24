from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Book, Borrowed
from forms import LoginForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def setup():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', password_hash=generate_password_hash('admin123'), is_admin=True)
        db.session.add(admin)
    if Book.query.count() == 0:
        db.session.add_all([
            Book(title='Python for Beginners'),
            Book(title='Flask Web Dev'),
            Book(title='SQL Mastery')
        ])
    db.session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash("Login successful ✅", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials ❌", "danger")
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash("You've been logged out.", "info")
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    books = Book.query.all()
    return render_template('dashboard.html', books=books)

@app.route('/borrow/<int:book_id>')
@login_required
def borrow(book_id):
    borrowed = Borrowed(book_id=book_id, user_id=current_user.id)
    db.session.add(borrowed)
    db.session.commit()
    session['last_borrowed'] = Book.query.get(book_id).title
    flash(f"Borrowed: {session['last_borrowed']} 📘", "success")
    return redirect(url_for('borrowed'))

@app.route('/borrowed')
@login_required
def borrowed():
    borrowed_books = Borrowed.query.filter_by(user_id=current_user.id).all()
    return render_template('borrowed.html', borrowed=borrowed_books, last=session.get('last_borrowed'))

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash("Access denied ❌", "danger")
        return redirect(url_for('dashboard'))
    all_borrowed = Borrowed.query.all()
    return render_template('borrowed.html', borrowed=all_borrowed, last=None)