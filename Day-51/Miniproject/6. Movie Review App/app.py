from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Review
from forms import LoginForm, ReviewForm
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
def create_tables():
    db.create_all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Login successful ✅', 'success')
            return redirect(url_for('movie_list'))
        else:
            flash('Invalid credentials ❌', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out 👋', 'info')
    return redirect(url_for('login'))

@app.route('/movies')
def movie_list():
    reviews = Review.query.all()
    return render_template('movies.html', reviews=reviews)

@app.route('/add_review', methods=['GET', 'POST'])
@login_required
def add_review():
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(
            movie_title=form.movie_title.data,
            rating=form.rating.data,
            comment=form.comment.data,
            user_id=current_user.id
        )
        db.session.add(new_review)
        db.session.commit()
        flash('Review submitted ✅', 'success')
        return redirect(url_for('movie_list'))
    return render_template('review.html', form=form)