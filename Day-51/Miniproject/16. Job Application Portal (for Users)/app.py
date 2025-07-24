from flask import Flask, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from forms import RegistrationForm, LoginForm, ApplicationForm
from models import db, User, Application
from jobs_data import job_list

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', jobs=job_list)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        flash('Login failed.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/apply/<job_id>', methods=['GET', 'POST'])
@login_required
def apply(job_id):
    job = next((job for job in job_list if job['id'] == job_id), None)
    if not job:
        flash("Job not found.", "warning")
        return redirect(url_for('index'))
    form = ApplicationForm()
    if form.validate_on_submit():
        app_entry = Application(
            user_id=current_user.id,
            job_id=job['id'],
            job_title=job['title'],
            resume_link=form.resume_link.data
        )
        db.session.add(app_entry)
        db.session.commit()
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('my_applications'))
    return render_template('apply.html', job=job, form=form)

@app.route('/my-applications')
@login_required
def my_applications():
    apps = Application.query.filter_by(user_id=current_user.id).all()
    return render_template('my_applications.html', applications=apps)
