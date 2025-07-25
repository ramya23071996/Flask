from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Simulated seat availability (True: Available, False: Booked)
seats = {
    "A1": True, "A2": False, "A3": True,
    "B1": True, "B2": True, "B3": False
}

@app.route('/')
def index():
    event_name = "Coimbatore Tech Talk"
    return render_template('seats.html', event=event_name, seat_labels=list(seats.keys()))

@app.route('/api/seats')
def get_seats():
    return jsonify(seats)