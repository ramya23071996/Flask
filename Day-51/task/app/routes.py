from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app.utils import log_failed_login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Account created. You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            user.login_count += 1
            user.last_login = datetime.now()
            db.session.commit()
            session['last_login'] = str(user.last_login)
            flash('Login successful!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            log_failed_login(request.remote_addr, form.email.data)
            flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

@auth.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username, count=current_user.login_count)

@auth.route('/settings')
@login_required
def settings():
    session['preferences'] = 'dark_mode'
    return render_template('settings.html', last_login=session.get('last_login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
