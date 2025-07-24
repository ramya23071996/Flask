from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Thread, Comment
from forms import LoginForm, ThreadForm, CommentForm
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
            flash("Login successful ✅", "success")
            return redirect(url_for('dashboard'))
        flash("Invalid credentials ❌", "danger")
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash("You've been logged out.", "info")
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = ThreadForm()
    if form.validate_on_submit():
        thread = Thread(title=form.title.data, user_id=current_user.id)
        db.session.add(thread)
        db.session.commit()
        flash("Thread created 🧵", "success")
        return redirect(url_for('dashboard'))
    my_threads = Thread.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', form=form, threads=my_threads)

@app.route('/thread/<int:id>', methods=['GET', 'POST'])
@login_required
def thread(id):
    thread = Thread.query.get_or_404(id)
    comments = Comment.query.filter_by(thread_id=id).all()
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, thread_id=id, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash("Comment posted 💬", "success")
        return redirect(url_for('thread', id=id))
    return render_template('thread.html', thread=thread, comments=comments, form=form)

if __name__ == '__main__':
    app.run(debug=True)