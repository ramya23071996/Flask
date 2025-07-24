from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, current_user, login_required
from app.models import db, User, Workout
from app.forms import RegisterForm, LoginForm, WorkoutForm, UpdateProfileForm
from datetime import date

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('main.register'))
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Welcome back!', 'success')
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'info')
    return redirect(url_for('main.login'))

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = WorkoutForm()
    if form.validate_on_submit():
        workout = Workout(
            user_id=current_user.id,
            workout_type=form.workout_type.data,
            duration=form.duration.data,
            date=date.today()
        )
        session['last_workout_type'] = form.workout_type.data
        db.session.add(workout)
        db.session.commit()
        flash('Workout logged!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('dashboard.html', form=form, last=session.get('last_workout_type'))

@main.route('/history')
@login_required
def history():
    logs = Workout.query.filter_by(user_id=current_user.id).order_by(Workout.date.desc()).all()
    return render_template('history.html', logs=logs)

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if current_user.check_password(form.current_password.data):
            current_user.set_password(form.new_password.data)
            db.session.commit()
            flash('Password updated successfully!', 'success')
        else:
            flash('Current password is incorrect.', 'danger')
    return render_template('profile.html', form=form)
