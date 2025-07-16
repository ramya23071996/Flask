from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# Simulated weather data (for demo purposes)
weather_data = {
    'chennai': {'temp_c': 34, 'temp_f': 93, 'condition': 'Sunny'},
    'mumbai': {'temp_c': 30, 'temp_f': 86, 'condition': 'Humid'},
    'delhi': {'temp_c': 28, 'temp_f': 82, 'condition': 'Cloudy'},
    'bangalore': {'temp_c': 25, 'temp_f': 77, 'condition': 'Rainy'}
}

# 1. /weather – form to enter city name
@app.route('/weather', methods=['GET', 'POST'])
def weather_form():
    if request.method == 'POST':
        city = request.form.get('city', '').strip().lower()
        return redirect(url_for('weather_report', city=city))

    return '''
    <h2>Check Weather Report</h2>
    <form method="POST">
        City: <input type="text" name="city"><br>
        <input type="submit" value="Get Weather">
    </form>
    '''

# 2. /weather-result – handled via redirect in POST above

# 3. /weather/<city> – dynamic weather report
@app.route('/weather/<city>')
def weather_report(city):
    unit = request.args.get('unit', 'metric').strip().lower()
    data = weather_data.get(city.lower())

    if not data:
        return f"<p>No weather data available for {escape(city.capitalize())}</p>"

    temp = data['temp_c'] if unit == 'metric' else data['temp_f']
    unit_label = '°C' if unit == 'metric' else '°F'
    condition = data['condition']

    return f"""
    <h3>Weather Report for {escape(city.capitalize())}</h3>
    <p>Temperature: {temp}{unit_label}</p>
    <p>Condition: {escape(condition)}</p>
    <p><em>Unit: {escape(unit.capitalize())}</em></p>
    """

# 4. /weather?unit=metric – query string supported in dynamic route

if __name__ == '__main__':
    app.run(debug=True)