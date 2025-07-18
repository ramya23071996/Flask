from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/achievements")
def achievements():
    current_year = datetime.now().year
    data = {
        2022: ["Launched new product", "Expanded to 3 countries"],
        2023: ["Won industry award", "Hit 1M users"],
        2024: ["Opened new HQ", "Achieved carbon neutrality"],
        2025: ["AI-powered dashboard released", "Record revenue growth"]
    }
    return render_template("achievements.html", data=data, current_year=current_year)

if __name__ == "__main__":
    app.run(debug=True)