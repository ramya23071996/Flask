from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. /method-check – returns current HTTP method
@app.route('/method-check', methods=['GET', 'POST'])
def method_check():
    return f"Current method: {request.method}"

# 2. /submit – allows only POST
@app.route('/submit', methods=['POST'])
def submit():
    return "Form submitted successfully via POST!"

# 3. /both-methods – supports GET and POST
@app.route('/both-methods', methods=['GET', 'POST'])
def both_methods():
    return f"You used {request.method} method."

# 4 & 5. /login – display form and return username on POST
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return f"Welcome, {username}!"
    return '''
    <form method="POST">
        Username: <input type="text" name="username">
        <input type="submit" value="Login">
    </form>
    '''

# 6. /admin – restrict to GET, warn if POST
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        return "⚠️ POST not allowed on /admin"
    return "Welcome to the admin panel (GET only)."

# 7. Print method in console during every request
@app.before_request
def log_method():
    print(f"Request method: {request.method}")

# 8. /feedback – form with textarea
@app.route('/feedback', methods=['GET'])
def feedback():
    return '''
    <form method="POST" action="/submit-feedback">
        <textarea name="comments" rows="4" cols="40"></textarea><br>
        <input type="submit" value="Send Feedback">
    </form>
    '''

# 8 continued. /submit-feedback – handle POST
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    comments = request.form.get('comments')
    return f"Thanks for your feedback: {comments}"

# 9. /post-button – button that triggers POST
@app.route('/post-button', methods=['GET'])
def post_button():
    return '''
    <form method="POST" action="/submit">
        <input type="submit" value="Submit via POST">
    </form>
    '''

# 10. /method-form – form with GET and POST options
@app.route('/method-form', methods=['GET', 'POST'])
def method_form():
    if request.method == 'POST':
        data = request.form.get('data')
        return f"POST received: {data}"
    elif request.method == 'GET' and 'data' in request.args:
        return f"GET received: {request.args.get('data')}"
    return '''
    <form method="GET">
        <input type="text" name="data">
        <input type="submit" value="Submit via GET">
    </form>
    <form method="POST">
        <input type="text" name="data">
        <input type="submit" value="Submit via POST">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)