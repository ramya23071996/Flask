from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# Sample warranty data
warranty_db = {
    'ABC123': {'product': 'Laptop X', 'warranty': '2 years'},
    'XYZ789': {'product': 'Smartphone Y', 'warranty': '1 year'},
    'LMN456': {'product': 'Tablet Z', 'warranty': '18 months'}
}

# 1. /check-warranty – form to enter serial number
@app.route('/check-warranty', methods=['GET', 'POST'])
def check_warranty():
    if request.method == 'POST':
        serial = request.form.get('serial', '').strip().upper()
        return redirect(url_for('warranty_result', serial=serial))

    return '''
    <h2>Warranty Checker</h2>
    <form method="POST">
        Enter Product Serial Number: <input type="text" name="serial"><br>
        <input type="submit" value="Check Warranty">
    </form>
    '''

# 2. /result?serial=ABC123 – query-based response
@app.route('/result')
def warranty_result():
    serial = request.args.get('serial', '').strip().upper()
    info = warranty_db.get(serial)

    if info:
        return f"""
        <h3>Warranty Details</h3>
        <p><strong>Product:</strong> {escape(info['product'])}</p>
        <p><strong>Warranty:</strong> {escape(info['warranty'])}</p>
        """
    return f"<p>No warranty information found for serial: {escape(serial)}</p>"

# 3. /warranty/<product> – dynamic route for product-specific warranty
@app.route('/warranty/<product>')
def warranty_by_product(product):
    product = product.lower()
    match = next((s for s, info in warranty_db.items() if info['product'].lower() == product), None)

    if match:
        info = warranty_db[match]
        return f"""
        <h3>Warranty for {escape(info['product'])}</h3>
        <p>Serial: {escape(match)}</p>
        <p>Warranty: {escape(info['warranty'])}</p>
        """
    return f"<p>No warranty found for product: {escape(product)}</p>"

# 4. Redirect already handled in /check-warranty POST

if __name__ == '__main__':
    app.run(debug=True)