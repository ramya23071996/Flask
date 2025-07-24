from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, JournalEntry

bp = Blueprint('bp', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('bp.view_journal'))
        flash("Invalid credentials")
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('bp.login'))

@bp.route('/journal')
@login_required
def view_journal():
    entries = JournalEntry.query.filter_by(user_id=current_user.id).all()
    return render_template('journal.html', entries=entries)

@bp.route('/journal/add', methods=['POST'])
@login_required
def add_entry():
    title = request.form['title']
    content = request.form['content']
    entry = JournalEntry(title=title, content=content, user_id=current_user.id)
    db.session.add(entry)
    db.session.commit()
    flash("Journal entry added.")
    return redirect(url_for('bp.view_journal'))

@bp.route('/journal/<int:entry_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        flash("Unauthorized access.")
        return redirect(url_for('bp.view_journal'))
    if request.method == 'POST':
        entry.update_entry(request.form['title'], request.form['content'])
        db.session.commit()
        flash("Entry updated.")
        return redirect(url_for('bp.view_journal'))
    return render_template('edit_entry.html', entry=entry)

@bp.route('/journal/<int:entry_id>/delete')
@login_required
def delete_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        flash("Unauthorized.")
        return redirect(url_for('bp.view_journal'))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted.")
    return redirect(url_for('bp.view_journal'))