from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def status():
    
    now = datetime.now()
    current_hour = now.hour
    if 9 <= current_hour < 18:
        return "<b>We are open!</b> <p>Come on in and say hello!</p><hr>"
    else:
        return "<b>Closed</b> <p>Our working hours are 9:00 to 18:00.</p><hr>"

@app.route("/contact")
def contact():
    return """
    <b>Contact Us</b>
    <p>Email: hello@mybusiness.com</p>
    <p>Phone: +91 98765 43210</p>
    <hr>
    """

if __name__ == "__main__":
    app.run(debug=True)