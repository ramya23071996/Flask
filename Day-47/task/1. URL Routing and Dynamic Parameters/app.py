from flask import Flask, escape

app = Flask(__name__)

# 1. /hello/<name>
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {escape(name)}!"

# 2. /square/<int:number>
@app.route('/square/<int:number>')
def square(number):
    return f"Square of {number} is {number ** 2}"

# 3. /greet/<name>/<int:age>
@app.route('/greet/<name>/<int:age>')
def greet(name, age):
    return f"Hi {escape(name)}, you are {age} years old!"

# 4. /status/<username>/<status>
@app.route('/status/<username>/<status>')
def status(username, status):
    return f"{escape(username)} is currently {escape(status)}."

# 5. /price/<float:amount>
@app.route('/price/<float:amount>')
def price(amount):
    return f"The price is ₹{amount:.2f}"

# 6. /profile/<username>
@app.route('/profile/<username>')
def profile(username):
    return f"""
    <html>
        <body>
            <h2>Profile</h2>
            <p>Username: <strong>{escape(username)}</strong></p>
        </body>
    </html>
    """

# 7. /math/<int:x>/<int:y>
@app.route('/math/<int:x>/<int:y>')
def math(x, y):
    return f"Sum: {x + y}, Difference: {x - y}, Product: {x * y}"

# 8. /file/<path:filename>
@app.route('/file/<path:filename>')
def file(filename):
    return f"Requested file path: {escape(filename)}"

# 9. /color/<string:color>
@app.route('/color/<string:color>')
def color(color):
    return f"<p style='color:{escape(color)};'>This is {escape(color)} text!</p>"

# 10. /language/<lang>
@app.route('/language/<lang>')
def language(lang):
    supported = ['python', 'javascript', 'html', 'css']
    if lang.lower() in supported:
        return f"{lang} is supported!"
    else:
        return f"{lang} is not supported."

# 11. /user/<username>
@app.route('/user/<username>')
def user(username):
    valid_users = ['ramya', 'arun', 'deepa']
    if username.lower() in valid_users:
        return f"Welcome, {username}!"
    else:
        return "User not found."

# 12. /country/<code>
@app.route('/country/<code>')
def country(code):
    countries = {
        'IN': 'India',
        'US': 'United States',
        'FR': 'France',
        'JP': 'Japan'
    }
    return countries.get(code.upper(), "Country code not recognized.")

# 13. /debug/<value>
@app.route('/debug/<value>')
def debug(value):
    print(f"Debug: Received value = {value}")
    return f"Value received: {value}"

# 14. /info/<name>/<int:score>
@app.route('/info/<name>/<int:score>')
def info(name, score):
    return f"""
    <html>
        <body>
            <h2>Student Info</h2>
            <p>Name: {escape(name)}</p>
            <p>Score: {score}</p>
        </body>
    </html>
    """

# 15. /error/<int:code>
@app.route('/error/<int:code>')
def error(code):
    messages = {
        404: "Page not found",
        500: "Internal server error",
        403: "Forbidden access"
    }
    return messages.get(code, "Unknown error code")


if __name__ == '__main__':
    app.run(debug=True)