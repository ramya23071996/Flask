from flask import Flask, render_template

app = Flask(__name__)

@app.route("/weather")
def weather():
    weather_data = {
        "location": "Coimbatore",
        "temperature": 34,
        "condition": "Sunny",
        "icon": "sun.png",
        "hourly": [28, 30, 32, 34, 33, 31, 29]
    }
    return render_template("weather.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)