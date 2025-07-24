from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Bug
from forms import LoginForm, BugForm
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
def create_tables():
    db.create_all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Login successful ✅', 'success')
            return redirect(url_for('submit_bug'))
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

@app.route('/submit_bug', methods=['GET', 'POST'])
@login_required
def submit_bug():
    form = BugForm()
    if form.validate_on_submit():
        bug = Bug(title=form.title.data, description=form.description.data, user_id=current_user.id)
        db.session.add(bug)
        db.session.commit()
        session['last_bug'] = bug.title
        flash('Bug report submitted 🐞', 'success')
        return redirect(url_for('my_bugs'))
    return render_template('submit_bug.html', form=form)

@app.route('/my_bugs')
@login_required
def my_bugs():
    bugs = Bug.query.filter_by(user_id=current_user.id).all()
    last_bug = session.get('last_bug')
    return render_template('my_bugs.html', bugs=bugs, last_bug=last_bug)

if __name__ == '__main__':
    app.run(debug=True)