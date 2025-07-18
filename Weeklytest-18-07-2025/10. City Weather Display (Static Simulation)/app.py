from flask import Flask, render_template, request

app = Flask(__name__)

# Static simulated weather data
weather_data = {
    "london": {"temp_c": 20, "condition": "cloudy"},
    "paris": {"temp_c": 25, "condition": "sunny"},
    "mumbai": {"temp_c": 30, "condition": "rainy"},
    "newyork": {"temp_c": 22, "condition": "sunny"}
}

@app.route('/weather/<city>')
def show_weather(city):
    city = city.lower()
    unit = request.args.get('unit', 'celsius')

    data = weather_data.get(city)
    if not data:
        return f"<h2>No weather data found for {city.title()}.</h2>"

    temperature = data["temp_c"]
    if unit == "fahrenheit":
        temperature = round((temperature * 9/5) + 32)

    return render_template('weather.html', city=city.title(), temperature=temperature, 
                           unit=unit, condition=data["condition"])

if __name__ == '__main__':
    app.run(debug=True)
