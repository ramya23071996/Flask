from flask import Flask, render_template_string

app = Flask(__name__)

# Hardcoded product database
products = {
    1: {"name": "Wireless Mouse", "price": 799, "in_stock": True},
    2: {"name": "Bluetooth Headphones", "price": 1999, "in_stock": False},
    3: {"name": "USB-C Charger", "price": 999, "in_stock": True}
}

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    print(f"Accessed: /product/{product_id}")
    product = products.get(product_id)
    if product:
        status = "In Stock ✅" if product["in_stock"] else "Out of Stock ❌"
        return f"""
        <html>
        <head><title>Product Info</title></head>
        <body style="font-family:sans-serif; padding:30px;">
            <h2>Product Details</h2>
            <p><strong>Name:</strong> {product['name']}</p>
            <p><strong>Price:</strong> ₹{product['price']}</p>
            <p><strong>Status:</strong> {status}</p>
        </body>
        </html>
        """
    else:
        return f"<h3>Product with ID {product_id} not found.</h3>"

@app.route("/products")
def list_products():
    print("Accessed: /products")
    table_rows = "".join([
        f"<tr><td>{pid}</td><td>{info['name']}</td></tr>"
        for pid, info in products.items()
    ])
    return f"""
    <html>
    <head>
        <title>Product List</title>
        <style>
            table {{ border-collapse: collapse; width: 60%; margin: auto; font-family: sans-serif; }}
            th, td {{ border: 1px solid #ccc; padding: 10px; text-align: left; }}
            th {{ background-color: #f0f0f0; }}
        </style>
    </head>
    <body>
        <h2 style="text-align:center;">All Products</h2>
        <table>
            <tr><th>Product ID</th><th>Name</th></tr>
            {table_rows}
        </table>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)