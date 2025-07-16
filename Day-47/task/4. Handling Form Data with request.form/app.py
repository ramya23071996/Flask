from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# 1 & 2. /contact – form to accept name and message
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()

        # 4. Basic validation
        if not name or not message:
            return "⚠️ Name and message cannot be empty."

        # 8. Print to terminal
        print(f"Contact Form Submitted: Name={name}, Message={message}")

        # 3. Redirect to thank you page
        return redirect(url_for('thankyou', name=name))

    return '''
    <form method="POST">
        Name: <input type="text" name="name"><br>
        Message: <textarea name="message"></textarea><br>
        <input type="submit" value="Send">
    </form>
    '''

# 3. /thankyou – show thank you page
@app.route('/thankyou')
def thankyou():
    name = request.args.get('name', 'Guest')
    return f"<h2>Thank you, {name}!</h2><p>Your message has been received.</p>"

# 5. Styled response with submitted data
@app.route('/styled-response', methods=['POST'])
def styled_response():
    name = request.form.get('name', 'Anonymous')
    message = request.form.get('message', '')
    return f"""
    <div style="border:1px solid #ccc; padding:10px;">
        <h3>Message from {name}</h3>
        <p>{message}</p>
    </div>
    """

# 7. /feedback – form with rating
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        rating = request.form.get('rating', 'N/A')
        comments = request.form.get('comments', '')
        print(f"Feedback Received: Rating={rating}, Comments={comments}")
        return f"Thanks for rating us {rating}/5!"
    
    return '''
    <form method="POST">
        Rating:
        <select name="rating">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
        </select><br>
        Comments: <textarea name="comments"></textarea><br>
        <input type="submit" value="Submit Feedback">
    </form>
    '''

# 9 & 10. /register – form with name, email, password
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = {
            'name': request.form.get('name', ''),
            'email': request.form.get('email', ''),
            'password': request.form.get('password', '')
        }
        print(f"Registration Data: {data}")
        return f"""
        <h3>Registration Successful</h3>
        <pre>{data}</pre>
        """
    
    return '''
    <form method="POST">
        Name: <input type="text" name="name"><br>
        Email: <input type="email" name="email"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Register">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)