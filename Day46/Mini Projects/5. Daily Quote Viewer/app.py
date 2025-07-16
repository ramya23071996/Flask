from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Hardcoded quotes for each day
quotes = {
    "monday": "Start your week strong 💪",
    "tuesday": "Keep the momentum going 🚀",
    "wednesday": "Midweek magic ✨",
    "thursday": "Stay focused and steady 🎯",
    "friday": "Finish with flair 🎉",
    "saturday": "Relax and recharge 🌿",
    "sunday": "Plan, reflect, and renew 🧘"
}

def style_quote(quote):
    return f"""
    <div style="font-family:Arial; background:#f4f4f4; padding:20px; border-radius:8px; width:60%; margin:auto; text-align:center;">
        <h2 style="color:#333;">{quote}</h2>
        <hr style="border-top:1px solid #ccc;">
    </div>
    """

@app.route("/")
def today_quote():
    day = datetime.now().strftime("%A").lower()  # e.g. 'monday'
    quote = quotes.get(day, "No quote found for today.")
    return style_quote(quote)

@app.route("/quote/<day>")
def quote_for_day(day):
    quote = quotes.get(day.lower(), "No quote found for that day.")
    return style_quote(quote)

if __name__ == "__main__":
    app.run(debug=True)