from flask import Flask

app = Flask(__name__)

@app.route("/")
def usage():
    return """
    <h2>BMI Calculator</h2>
    <p>Usage: /bmi/&lt;weight_kg&gt;/&lt;height_cm&gt;</p>
    <p>Example: <a href='/bmi/70/170'>/bmi/70/170</a></p>
    <hr>
    """

@app.route("/bmi/<weight>/<height>")
def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height) / 100  # Convert cm to meters
        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        return f"""
        <h3>Your BMI is {bmi}</h3>
        <p>Category: <b>{category}</b></p>
        <hr>
        """
    except ValueError:
        return "<p>Please enter numeric values only for weight and height.</p><hr>"
    
    