from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

@app.route("/")
def index():
    return render_template("index.html", initial_count=user_count["count"])

@app.route("/api/users/count")
def get_user_count():
    # Simulate dynamic count increase (for demo)
    user_count["count"] += random.randint(0, 1)
    return jsonify(user_count)

if __name__ == "__main__":
    app.run(debug=True)