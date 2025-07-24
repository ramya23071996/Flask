from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User

bp = Blueprint('bp', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('bp.admin'))
        flash("Invalid credentials")
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('bp.login'))

@bp.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash("Admin only access!")
        return redirect(url_for('bp.login'))
    return render_template('admin.html', user=current_user)