from flask import Flask

app = Flask(__name__)

# Hour-based advice dictionary (basic rotation logic)
reminders = {
    "morning": "Start your day with a glass of water and light stretches.",
    "midday": "Take a short walk and don’t forget to hydrate!",
    "afternoon": "Look away from your screen and roll your shoulders.",
    "evening": "Wind down with deep breaths or a short meditation.",
    "late": "Avoid caffeine, and prep for a restful sleep."
}

@app.route("/reminder/<int:hour>")
def health_reminder(hour):
    print(f"Accessed: /reminder/{hour}")
    if hour < 0 or hour > 23:
        msg = "Invalid hour! Please enter a value between 0 and 23."
    elif hour < 10:
        msg = reminders["morning"]
    elif hour < 13:
        msg = reminders["midday"]
    elif hour < 17:
        msg = reminders["afternoon"]
    elif hour < 21:
        msg = reminders["evening"]
    else:
        msg = reminders["late"]

    return f"""
    <html>
    <head>
        <title>Health Reminder</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background-color: #e8f5e9; padding: 40px; }}
            h1 {{ color: #2e7d32; }}
            p {{ font-size: 1.3em; color: #388e3c; }}
        </style>
    </head>
    <body>
        <h1>Health Reminder 🩺</h1>
        <p>{msg}</p>
    </body>
    </html>
    """

@app.route("/reminder/help")
def reminder_help():
    print("Accessed: /reminder/help")
    return """
    <html>
    <head>
        <title>Reminder Help</title>
        <style>
            body { font-family: Verdana, sans-serif; background-color: #fffde7; padding: 30px; }
            h2 { color: #fbc02d; }
            ul { font-size: 1.2em; color: #f57f17; }
        </style>
    </head>
    <body>
        <h2>Health Reminder Usage</h2>
        <ul>
            <li>Use the format: <strong>/reminder/&lt;hour&gt;</strong></li>
            <li>Valid hour range: <strong>0</strong> to <strong>23</strong></li>
            <li>Example: <i>/reminder/9</i> → Morning hydration advice</li>
        </ul>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)