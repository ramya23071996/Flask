from flask import Flask

app = Flask(__name__)

@app.route("/hello/<name>")
def say_hello(name):
    return f"<h2>Hello, {name}!</h2><hr>"

@app.route("/greet/<name>/<time>")
def greet(name, time):
    time = time.lower()
    if "morning" in time:
        greeting = "Good Morning"
    elif "afternoon" in time:
        greeting = "Good Afternoon"
    elif "evening" in time:
        greeting = "Good Evening"
    else:
        greeting = "Hello"

    return f"<h2>{greeting}, {name}!</h2><hr>"

if __name__ == "__main__":
    app.run(debug=True)