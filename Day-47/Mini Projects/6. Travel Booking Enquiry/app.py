from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory booking store
bookings = []

# 1. /booking – form with name, destination, travel date
@app.route('/booking', methods=['GET'])
def booking_form():
    return '''
    <h2>Travel Booking Enquiry</h2>
    <form method="POST" action="/booking">
        Name: <input type="text" name="name"><br>
        Destination: 
        <select name="destination">
            <option value="paris">Paris</option>
            <option value="tokyo">Tokyo</option>
            <option value="newyork">New York</option>
        </select><br>
        Travel Date: <input type="date" name="date"><br>
        <input type="submit" value="Submit Enquiry">
    </form>
    '''

# 2. Handle POST and redirect to dynamic confirmation
@app.route('/booking', methods=['POST'])
def booking_submit():
    name = request.form.get('name', '').strip()
    destination = request.form.get('destination', '').strip().lower()
    date = request.form.get('date', '').strip()

    # Store booking
    bookings.append({
        'name': name,
        'destination': destination,
        'date': date
    })

    # Redirect to confirmation page
    return redirect(url_for('booking_confirm', name=name))

# 3. /booking/confirm/<name> – dynamic confirmation
@app.route('/booking/confirm/<name>')
def booking_confirm(name):
    match = next((b for b in bookings if b['name'].lower() == name.lower()), None)
    if match:
        return f"""
        <h3>Booking Confirmed</h3>
        <p>Name: {escape(match['name'])}</p>
        <p>Destination: {escape(match['destination'].capitalize())}</p>
        <p>Travel Date: {escape(match['date'])}</p>
        """
    return f"<p>No booking found for {escape(name)}</p>"

# 4. /deals?destination=paris – filter deals by destination
@app.route('/deals')
def travel_deals():
    destination = request.args.get('destination', '').strip().lower()
    sample_deals = {
        'paris': ['Eiffel Tower Tour', 'Seine River Cruise'],
        'tokyo': ['Cherry Blossom Walk', 'Mount Fuji Day Trip'],
        'newyork': ['Statue of Liberty Visit', 'Broadway Show']
    }

    deals = sample_deals.get(destination)
    if not deals:
        return f"<p>No deals available for {escape(destination.capitalize())}</p>"

    items = "".join([f"<li>{escape(deal)}</li>" for deal in deals])
    return f"<h3>Deals for {escape(destination.capitalize())}</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)