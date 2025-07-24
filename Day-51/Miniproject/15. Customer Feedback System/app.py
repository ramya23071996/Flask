from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Feedback
from forms import LoginForm, FeedbackForm
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
    feedback = Feedback.query.filter_by(user_id=current_user.id).all()
    all_feedback = Feedback.query.all() if current_user.is_admin else None
    return render_template('dashboard.html', feedback=feedback, all_feedback=all_feedback)

@app.route('/submit', methods=['GET', 'POST'])
@login_required
def submit():
    form = FeedbackForm()
    if form.validate_on_submit():
        fb = Feedback(content=form.content.data, user_id=current_user.id)
        db.session.add(fb)
        db.session.commit()
        flash("Thank you for your feedback! 🙌", "success")
        return redirect(url_for('dashboard'))
    return render_template('submit_feedback.html', form=form)