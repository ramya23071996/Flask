from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Simulated count
message_count = {"count": 52}

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/api/messages/count')
def message_count_api():
    return jsonify(message_count)