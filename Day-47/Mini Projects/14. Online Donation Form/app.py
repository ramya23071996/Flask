from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory donation log
donations = []

# 1. /donate – form for name, amount, and purpose
@app.route('/donate', methods=['GET'])
def donate_form():
    return '''
    <h2>Make a Donation</h2>
    <form method="POST" action="/donate-confirm">
        Name: <input type="text" name="name"><br>
        Amount: <input type="number" name="amount" step="0.01"><br>
        Purpose:
        <select name="purpose">
            <option value="education">Education</option>
            <option value="healthcare">Healthcare</option>
            <option value="environment">Environment</option>
        </select><br>
        <input type="submit" value="Donate">
    </form>
    '''

# 2. /donate-confirm – handle POST and redirect
@app.route('/donate-confirm', methods=['POST'])
def donate_confirm():
    name = request.form.get('name', 'Anonymous').strip()
    amount = request.form.get('amount', '0').strip()
    purpose = request.form.get('purpose', 'general').strip().lower()

    # Store donation
    donations.append({
        'name': name,
        'amount': float(amount),
        'purpose': purpose
    })

    # Redirect to thank-you page
    return redirect(url_for('thank_donor', name=name))

# 3. /thank-donor/<name> – personalized thank-you
@app.route('/thank-donor/<name>')
def thank_donor(name):
    return f"<h3>Thank you, {escape(name)}! Your donation is greatly appreciated.</h3>"

# 4. /donations?purpose=education – filter donations by purpose
@app.route('/donations')
def view_donations():
    purpose = request.args.get('purpose', '').strip().lower()
    filtered = [d for d in donations if d['purpose'] == purpose] if purpose else donations

    if not filtered:
        return f"<p>No donations found for purpose: {escape(purpose)}</p>"

    items = "".join([
        f"<li>{escape(d['name'])} donated ₹{d['amount']:.2f} for {escape(d['purpose'].capitalize())}</li>"
        for d in filtered
    ])
    return f"<h3>Donations</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)