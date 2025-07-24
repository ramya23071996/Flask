from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Product
from forms import LoginForm, ProductForm
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
def create_admin():
    db.create_all()
    if not User.query.filter_by(email='admin@example.com').first():
        admin = User(email='admin@example.com', password_hash=generate_password_hash('admin123'), is_admin=True)
        db.session.add(admin)
        db.session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash("Login successful ✅", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials ❌", "danger")
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out 👋", "info")
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        flash("Access denied ❌", "danger")
        return redirect(url_for('login'))
    products = Product.query.all()
    return render_template('dashboard.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_product():
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(
            name=form.name.data,
            price=form.price.data,
            description=form.description.data
        )
        db.session.add(new_product)
        db.session.commit()
        flash("Product added 🛒", "success")
        return redirect(url_for('dashboard'))
    return render_template('add_product.html', form=form)

@app.route('/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.description = form.description.data
        db.session.commit()
        flash("Product updated ✏️", "success")
        return redirect(url_for('dashboard'))
    return render_template('edit_product.html', form=form)

@app.route('/delete/<int:product_id>')
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash("Product deleted 🗑️", "info")
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)