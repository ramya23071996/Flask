from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simulated currency rates (e.g., 1 USD to X)
rates = {
    "INR": 83.2,
    "EUR": 0.91,
    "GBP": 0.78,
    "JPY": 149.5
}

@app.route('/')
def index():
    return render_template('converter.html', currencies=rates.keys())

@app.route('/api/convert')
def convert():
    try:
        amount = float(request.args.get('amount'))
        to_currency = request.args.get('to', 'INR')
        rate = rates.get(to_currency.upper())
        if rate:
            return jsonify({"result": round(amount * rate, 2)})
        else:
            return jsonify({"error": "Invalid currency"}), 400
    except Exception:
        return jsonify({"error": "Invalid input"}), 400