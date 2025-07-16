from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory subscription log
subscriptions = []

# 1. /subscribe – GET form with name and email
@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        name = request.form.get('name', 'Anonymous').strip()
        email = request.form.get('email', '').strip()
        month = request.form.get('month', 'Unknown').strip()

        # Store subscription
        subscriptions.append({
            'name': name,
            'email': email,
            'month': month
        })

        # Redirect to dynamic thank-you page
        return redirect(url_for('thanks_subscriber', name=name))

    return '''
    <h2>Subscribe to Our Newsletter</h2>
    <form method="POST">
        Name: <input type="text" name="name"><br>
        Email: <input type="email" name="email"><br>
        Subscription Month:
        <select name="month">
            <option value="January">January</option>
            <option value="February">February</option>
            <option value="March">March</option>
            <option value="April">April</option>
            <option value="May">May</option>
            <option value="June">June</option>
            <option value="July">July</option>
            <option value="August">August</option>
            <option value="September">September</option>
            <option value="October">October</option>
            <option value="November">November</option>
            <option value="December">December</option>
        </select><br>
        <input type="submit" value="Subscribe">
    </form>
    '''

# 2. /thanks/<name> – dynamic confirmation
@app.route('/thanks/<name>')
def thanks_subscriber(name):
    return f"<h3>Thank you, {escape(name)}! You’ve successfully subscribed to our newsletter.</h3>"

# 3. /subscribers?month=July – filter by month
@app.route('/subscribers')
def subscribers_by_month():
    month = request.args.get('month', '').strip()
    filtered = [s for s in subscriptions if s['month'].lower() == month.lower()] if month else subscriptions

    if not filtered:
        return f"<p>No subscribers found for month: {escape(month)}</p>"

    items = "".join([
        f"<li>{escape(s['name'])} – {escape(s['email'])} ({escape(s['month'])})</li>"
        for s in filtered
    ])
    return f"<h3>Subscribers for {escape(month)}</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)