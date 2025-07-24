from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Course, Enrollment
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
    # Preload courses if none exist
    if Course.query.count() == 0:
        db.session.add_all([
            Course(name='Python Fundamentals'),
            Course(name='Web Development'),
            Course(name='Database Design')
        ])
        db.session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Login successful ✅', 'success')
            return redirect(url_for('courses'))
        else:
            flash('Invalid credentials ❌', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('Logged out 👋', 'info')
    return redirect(url_for('login'))

@app.route('/courses')
@login_required
def courses():
    all_courses = Course.query.all()
    return render_template('courses.html', courses=all_courses)

@app.route('/enroll/<int:course_id>')
@login_required
def enroll(course_id):
    existing = Enrollment.query.filter_by(user_id=current_user.id, course_id=course_id).first()
    if existing:
        flash('Already enrolled in this course 🔁', 'warning')
    else:
        new_enrollment = Enrollment(user_id=current_user.id, course_id=course_id)
        db.session.add(new_enrollment)
        db.session.commit()
        flash('Enrolled successfully 🎓', 'success')
    return redirect(url_for('history'))

@app.route('/history')
@login_required
def history():
    enrollments = Enrollment.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html', enrollments=enrollments)