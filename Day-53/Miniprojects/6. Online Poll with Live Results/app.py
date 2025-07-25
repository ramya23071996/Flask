from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_cors import CORS
from flask import session
import random

app = Flask(__name__)
app.secret_key = "super_secret_key"
CORS(app)

# Poll question and options
poll = {
    "question": "What's your favorite programming language?",
    "options": {
        "Python": 0,
        "JavaScript": 0,
        "C++": 0,
        "Go": 0
    }
}

@app.route("/")
def index():
    return render_template("index.html", poll=poll)

@app.route("/api/poll", methods=["GET"])
def get_poll():
    return jsonify(poll)

@app.route("/api/vote", methods=["POST"])
def vote():
    if session.get("voted"):
        return jsonify({"error": "Already voted"}), 403

    data = request.get_json()
    option = data.get("option")
    if option in poll["options"]:
        poll["options"][option] += 1
        session["voted"] = True
        return jsonify({"message": "Vote recorded"}), 200
    return jsonify({"error": "Invalid option"}), 400

@app.route("/api/results", methods=["GET"])
def results():
    return jsonify(poll["options"])

if __name__ == "__main__":
    app.run(debug=True)