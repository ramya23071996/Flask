from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Appointment
from forms import LoginForm, AppointmentForm
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
    appointments = Appointment.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', appointments=appointments)

@app.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    form = AppointmentForm()
    if form.validate_on_submit():
        appt = Appointment(
            date=form.date.data,
            time=form.time.data,
            reason=form.reason.data,
            user_id=current_user.id
        )
        db.session.add(appt)
        db.session.commit()
        flash('Appointment booked 🗓️', 'success')
        return redirect(url_for('dashboard'))
    return render_template('edit_appointment.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    appt = Appointment.query.get_or_404(id)
    if appt.user_id != current_user.id:
        flash('Access denied ❌', 'danger')
        return redirect(url_for('dashboard'))
    form = AppointmentForm(obj=appt)
    if form.validate_on_submit():
        appt.date = form.date.data
        appt.time = form.time.data
        appt.reason = form.reason.data
        db.session.commit()
        flash('Appointment updated 📝', 'success')
        return redirect(url_for('dashboard'))
    return render_template('edit_appointment.html', form=form)

@app.route('/cancel/<int:id>')
@login_required
def cancel(id):
    appt = Appointment.query.get_or_404(id)
    if appt.user_id == current_user.id:
        db.session.delete(appt)
        db.session.commit()
        flash('Appointment cancelled ❌', 'info')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)