
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/time')
def get_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    return jsonify({'time': current_time})

if __name__ == '__main__':
    app.run(debug=True)