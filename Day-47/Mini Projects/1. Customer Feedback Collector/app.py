from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory feedback store (for demo purposes)
feedback_store = []

# 1. /feedback-form – form to collect feedback
@app.route('/feedback-form', methods=['GET'])
def feedback_form():
    return '''
    <h2>Customer Feedback</h2>
    <form method="POST" action="/submit-feedback">
        Name: <input type="text" name="name"><br>
        Email: <input type="email" name="email"><br>
        Message: <textarea name="message"></textarea><br>
        <input type="submit" value="Submit Feedback">
    </form>
    '''

# 2. /submit-feedback – handle POST and redirect
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()

    # Store feedback
    feedback_store.append({
        'name': name,
        'email': email,
        'message': message
    })

    # Redirect to thank-you page with name as query param
    return redirect(url_for('thank_you', name=name))

# 3. /thank-you – thank the user
@app.route('/thank-you')
def thank_you():
    name = request.args.get('name', 'Guest')
    return f"<h3>Thank you, {escape(name)}! Your feedback has been received.</h3>"

# 4. /feedbacks?user=name – filter feedbacks by name
@app.route('/feedbacks')
def feedbacks():
    user = request.args.get('user', '').strip().lower()
    filtered = [f for f in feedback_store if f['name'].lower() == user] if user else feedback_store

    if not filtered:
        return f"<p>No feedback found for user: {escape(user)}</p>"

    items = "".join([
        f"<li><strong>{escape(f['name'])}</strong> ({escape(f['email'])}): {escape(f['message'])}</li>"
        for f in filtered
    ])
    return f"<h3>Feedbacks</h3><ul>{items}</ul>"

# 5. /user/<username> – show user-specific data
@app.route('/user/<username>')
def user_profile(username):
    user_feedbacks = [f for f in feedback_store if f['name'].lower() == username.lower()]
    if not user_feedbacks:
        return f"<p>No feedback found for user: {escape(username)}</p>"

    items = "".join([
        f"<li>{escape(f['message'])} (Email: {escape(f['email'])})</li>"
        for f in user_feedbacks
    ])
    return f"<h3>Feedback from {escape(username)}</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)