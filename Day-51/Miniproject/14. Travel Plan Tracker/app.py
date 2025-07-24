from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, TravelPlan
from forms import LoginForm, PlanForm
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Login successful ✅', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials ❌', 'danger')
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
    plans = TravelPlan.query.filter_by(user_id=current_user.id).all()
    last_country = session.get('last_search')
    return render_template('dashboard.html', plans=plans, last_country=last_country, total=len(plans))

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_plan():
    form = PlanForm()
    if form.validate_on_submit():
        plan = TravelPlan(
            country=form.country.data,
            date=form.date.data,
            reason=form.reason.data,
            user_id=current_user.id
        )
        db.session.add(plan)
        db.session.commit()
        session['last_search'] = form.country.data
        flash('Plan saved ✈️', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_plan.html', form=form)