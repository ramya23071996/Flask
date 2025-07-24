from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, RSVP

bp = Blueprint('bp', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('bp.dashboard'))
        flash("Invalid credentials.")
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    session.pop('recent_event', None)
    return redirect(url_for('bp.login'))

@bp.route('/rsvp', methods=['GET', 'POST'])
@login_required
def rsvp():
    if request.method == 'POST':
        event = request.form['event_name']
        status = request.form['status']
        rsvp = RSVP.query.filter_by(user_id=current_user.id, event_name=event).first()
        if rsvp:
            rsvp.update_status(status)
        else:
            rsvp = RSVP(event_name=event, status=status, user_id=current_user.id)
            db.session.add(rsvp)
        db.session.commit()
        session['recent_event'] = event
        flash(f"RSVP updated for {event}")
        return redirect(url_for('bp.dashboard'))
    return render_template('rsvp.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    rsvps = RSVP.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', rsvps=rsvps, recent=session.get('recent_event'))