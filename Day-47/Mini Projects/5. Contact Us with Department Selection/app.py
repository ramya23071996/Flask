from flask import Flask, request, redirect, url_for, escape, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# In-memory contact store
contacts = []

# 1. /contact – GET form with department selection
@app.route('/contact', methods=['GET'])
def contact():
    messages = get_flashed_messages()
    flash_msg = f"<p style='color:green;'>{messages[0]}</p>" if messages else ""

    return f'''
    <h2>Contact Us</h2>
    {flash_msg}
    <form method="POST" action="/submit?source=homepage">
        Name: <input type="text" name="name"><br>
        Email: <input type="email" name="email"><br>
        Message: <textarea name="message"></textarea><br>
        Department:
        <select name="department">
            <option value="sales">Sales</option>
            <option value="support">Support</option>
            <option value="hr">HR</option>
        </select><br>
        <input type="submit" value="Send">
    </form>
    '''

# 2. /submit – handle POST, use request.form and request.args
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()
    department = request.form.get('department', '').strip().lower()
    source = request.args.get('source', 'unknown')

    # Store contact
    contacts.append({
        'name': name,
        'email': email,
        'message': message,
        'department': department,
        'source': source
    })

    # Flash confirmation and redirect
    flash(f"Thank you, {name}! Your message has been sent to the {department.capitalize()} department.")
    return redirect(url_for('thank_you'))

# 3. /contact/thank-you – show flash message
@app.route('/contact/thank-you')
def thank_you():
    messages = get_flashed_messages()
    return f"<h3>{messages[0] if messages else 'Thank you!'}</h3>"

# 4. /contact/<department> – dynamic route for department-specific view
@app.route('/contact/<department>')
def contact_department(department):
    filtered = [c for c in contacts if c['department'] == department.lower()]
    if not filtered:
        return f"<p>No messages found for {escape(department)} department.</p>"

    items = "".join([
        f"<li>{escape(c['name'])} ({escape(c['email'])}): {escape(c['message'])}</li>"
        for c in filtered
    ])
    return f"<h3>Messages for {escape(department.capitalize())} Department</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)