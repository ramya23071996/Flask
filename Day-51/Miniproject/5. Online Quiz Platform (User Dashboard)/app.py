from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Score
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

# Setup route
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
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials ❌', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out 👋', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    scores = Score.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', scores=scores)

@app.route('/quiz')
@login_required
def quiz():
    return render_template('quiz.html')

def calculate_score(form_data):
    # Stub logic (you can customize this)
    score = sum(int(form_data.get(q, 0)) for q in form_data)
    return score

@app.route('/submit_quiz', methods=['POST'])
@login_required
def submit_quiz():
    score = calculate_score(request.form)
    new_score = Score(user_id=current_user.id, quiz_name='General Knowledge', score_value=score)
    db.session.add(new_score)
    db.session.commit()
    flash('Quiz submitted successfully 🎉', 'success')
    return redirect(url_for('results'))

@app.route('/results')
@login_required
def results():
    scores = Score.query.filter_by(user_id=current_user.id).all()
    return render_template('results.html', scores=scores)

if __name__ == '__main__':
    app.run(debug=True)