from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import RegistrationForm, LoginForm, TaskForm
from app.models import User, Task
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.task_list'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Registered! Please login.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.task_list'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main.task_list'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'info')
    return redirect(url_for('main.login'))

@main.route('/tasks')
@login_required
def task_list():
    tasks = Task.query.filter_by(owner=current_user).all()
    return render_template('tasks.html', tasks=tasks)

@main.route('/tasks/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, due_date=form.due_date.data, is_complete=form.is_complete.data, owner=current_user)
        db.session.add(task)
        db.session.commit()
        flash('Task created!', 'success')
        return redirect(url_for('main.task_list'))
    return render_template('new_task.html', form=form)

@main.route('/tasks/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    task = Task.query.get_or_404(id)
    if task.owner != current_user:
        flash('Not authorized.', 'danger')
        return redirect(url_for('main.task_list'))
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.due_date = form.due_date.data
        task.is_complete = form.is_complete.data
        db.session.commit()
        flash('Task updated!', 'success')
        return redirect(url_for('main.task_list'))
    return render_template('edit_task.html', form=form)

@main.route('/')
def index():
    return redirect(url_for('main.task_list'))
