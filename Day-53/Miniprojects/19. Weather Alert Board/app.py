from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Simulated alert data
alerts = {
    "Coimbatore": [
        "Thunderstorm warning for tonight",
        "Heat index above normal",
        "Light showers expected tomorrow"
    ],
    "Delhi": [
        "Air quality advisory in effect",
        "Possible rain in northwest zones"
    ]
}

@app.route('/')
def index():
    region = "Coimbatore"  # Example region
    return render_template("alerts.html", region=region)

@app.route('/api/weather/alerts')
def get_weather_alerts():
    region = "Coimbatore"
    return jsonify({"region": region, "alerts": alerts.get(region, [])})