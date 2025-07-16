from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory RSVP store (for demo purposes)
guest_list = []

# 1. /rsvp – GET form for RSVP
@app.route('/rsvp', methods=['GET'])
def rsvp():
    return '''
    <h2>RSVP for the Event</h2>
    <form method="POST" action="/rsvp-confirm">
        Name: <input type="text" name="name"><br>
        Email: <input type="email" name="email"><br>
        Attending:
        <select name="attending">
            <option value="yes">Yes</option>
            <option value="no">No</option>
        </select><br>
        <input type="submit" value="Submit RSVP">
    </form>
    '''

# 2. /rsvp-confirm – handle POST and redirect
@app.route('/rsvp-confirm', methods=['POST'])
def rsvp_confirm():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    attending = request.form.get('attending', 'no').strip().lower()

    # Store RSVP
    guest_list.append({
        'name': name,
        'email': email,
        'attending': attending
    })

    # Redirect to personalized thank-you page
    return redirect(url_for('thank_you_guest', name=name))

# 3. /thank-you/<name> – personalized thank-you
@app.route('/thank-you/<name>')
def thank_you_guest(name):
    return f"<h3>Thank you, {escape(name)}! Your RSVP has been recorded.</h3>"

# 4. /guests?attending=yes – list attendees
@app.route('/guests')
def guests():
    attending = request.args.get('attending', '').strip().lower()
    filtered = [g for g in guest_list if g['attending'] == attending] if attending else guest_list

    if not filtered:
        return f"<p>No guests found with attending status: {escape(attending)}</p>"

    items = "".join([
        f"<li>{escape(g['name'])} ({escape(g['email'])}) – Attending: {escape(g['attending'])}</li>"
        for g in filtered
    ])
    return f"<h3>Guest List</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)