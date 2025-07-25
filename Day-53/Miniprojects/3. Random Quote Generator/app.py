from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "Simplicity is the soul of efficiency.",
    "Make it work, make it right, make it fast.",
    "Talk is cheap. Show me the code.",
    "Programs must be written for people to read, and only incidentally for machines to execute."
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)