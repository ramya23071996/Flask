from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from forms import RegisterForm, LoginForm, ExpenseForm, LimitForm
from models import db, User, Expense
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'budget-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget.db'

os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

db.init_app(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = ExpenseForm()
    limit_form = LimitForm()
    if form.validate_on_submit():
        expense = Expense(amount=form.amount.data, category=form.category.data, user_id=current_user.id)
        db.session.add(expense)
        db.session.commit()
        flash('Expense added.')

        # Check if exceeds monthly limit
        limit = session.get('monthly_limit')
        if limit:
            total = sum(e.amount for e in Expense.query.filter_by(user_id=current_user.id).all())
            if total > float(limit):
                flash('⚠️ Warning: You have exceeded your monthly budget limit!')

        return redirect(url_for('dashboard'))

    if limit_form.validate_on_submit():
        session['monthly_limit'] = limit_form.limit.data
        flash(f'Monthly limit set to ₹{limit_form.limit.data}')
        return redirect(url_for('dashboard'))

    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    total_spent = sum(e.amount for e in expenses)
    return render_template('dashboard.html', form=form, limit_form=limit_form, expenses=expenses, total=total_spent, limit=session.get('monthly_limit'))

@app.route('/summary')

@login_required
def summary():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    summary = {}
    for e in expenses:
        summary[e.category] = summary.get(e.category, 0) + e.amount
    return render_template('summary.html', summary=summary)

if __name__ == '__main__':
    with app.app_context():
         db.create_all() 
    app.run(debug=True)