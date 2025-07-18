from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/event")
def event():
    event_name = "Ramya Dev Summit"
    event_date = datetime(2025, 7, 25, 10, 0)  # YYYY, MM, DD, HH, MM
    now = datetime.now()
    event_started = now >= event_date
    return render_template("event.html", event_name=event_name, event_date=event_date, event_started=event_started)

if __name__ == "__main__":
    app.run(debug=True)