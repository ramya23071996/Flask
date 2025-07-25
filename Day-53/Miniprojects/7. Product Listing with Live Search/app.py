from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Wireless Mouse", "price": "$25"},
    {"id": 2, "name": "Keyboard", "price": "$30"},
    {"id": 3, "name": "USB-C Charger", "price": "$20"},
    {"id": 4, "name": "Noise-Canceling Headphones", "price": "$80"},
    {"id": 5, "name": "Laptop Stand", "price": "$40"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)