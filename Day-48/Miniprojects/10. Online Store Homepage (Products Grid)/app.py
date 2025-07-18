from flask import Flask, render_template

app = Flask(__name__)

@app.route("/products")
def products():
    items = [
        {"name": "Laptop", "price": 75000, "in_stock": True, "image": "laptop.jpg"},
        {"name": "Headphones", "price": 2500, "in_stock": False, "image": "headphones.jpg"},
        {"name": "Camera", "price": 42000, "in_stock": True, "image": "camera.jpg"}
    ]
    return render_template("products.html", products=items)

if __name__ == "__main__":
    app.run(debug=True)