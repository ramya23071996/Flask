from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',
                           username="Mahesh",
                           logged_in=True,
                           skills=["Python", "Flask", "Jinja"],
                           current_date=datetime.now(),
                           name="Mahesh",
                           role="admin")

@app.route('/scores')
def scores():
    score_list = [95, 67, 88, 45, 76]
    return render_template('scores.html', scores=score_list)

@app.route('/products')
def products():
    product_list = [
        {"name": "Laptop", "price": "$999", "description": "High-performance laptop with 16GB RAM."},
        {"name": "Mouse", "price": "$25", "description": "Wireless ergonomic mouse."},
        {"name": "Keyboard", "price": "$45", "description": "Mechanical keyboard with RGB lighting."}
    ]
    return render_template('products.html', products=product_list)

@app.route('/dictionary')
def dictionary():
    info = {"Python": "Programming Language", "Flask": "Web Framework", "Jinja": "Template Engine"}
    return render_template('dictionary.html', info=info)