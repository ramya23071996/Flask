from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    return render_template('clock.html', hour=now.hour, minute=now.minute, second=now.second)

@app.route('/api/time')
def get_time():
    now = datetime.now()
    return jsonify({
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second
    })