from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, JournalEntry
from forms import LoginForm, EntryForm
from config import Config
from datetime import datetime

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
            session['login_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            flash('Login successful ✅', 'success')
            return redirect(url_for('dashboard'))
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

@app.route('/dashboard')
@login_required
def dashboard():
    entries = JournalEntry.query.filter_by(user_id=current_user.id).all()
    login_time = session.get('login_time')
    return render_template('dashboard.html', entries=entries, login_time=login_time)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_entry():
    form = EntryForm()
    if form.validate_on_submit():
        entry = JournalEntry(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(entry)
        db.session.commit()
        flash('Entry added ✨', 'success')
        return redirect(url_for('dashboard'))
    return render_template('edit_entry.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_entry(id):
    entry = JournalEntry.query.get_or_404(id)
    if entry.user_id != current_user.id:
        flash('Access denied ❌', 'danger')
        return redirect(url_for('dashboard'))
    form = EntryForm(obj=entry)
    if form.validate_on_submit():
        entry.title = form.title.data
        entry.content = form.content.data
        db.session.commit()
        flash('Entry updated 📝', 'success')
        return redirect(url_for('dashboard'))
    return render_template('edit_entry.html', form=form)

@app.route('/delete/<int:id>')
@login_required
def delete_entry(id):
    entry = JournalEntry.query.get_or_404(id)
    if entry.user_id != current_user.id:
        flash('Access denied ❌', 'danger')
    else:
        db.session.delete(entry)
        db.session.commit()
        flash('Entry deleted 🗑️', 'info')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)