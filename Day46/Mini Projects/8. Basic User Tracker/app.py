from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")
def greet_user(name):
    print(f"Accessed: /user/{name}")  # Console log
    return f"Welcome, {name}!"

@app.route("/user/<name>/location/<city>")
def user_location(name, city):
    print(f"Accessed: /user/{name}/location/{city}")  # Console log
    return f"Hi {name}, how is {city}?"

if __name__ == "__main__":
    app.run(debug=True)