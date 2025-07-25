from flask import Flask, render_template, jsonify
import random, time

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html", location="Coimbatore", title="Live Weather Dashboard")

@app.route("/api/weather")
def weather():
    weather_data = {
        "temperature": random.randint(25, 35),
        "humidity": random.randint(40, 80),
        "status": random.choice(["Sunny", "Cloudy", "Rainy", "Windy"]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug=True)