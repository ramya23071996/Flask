from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
start_time = time.time()

@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello, API world!'}), 200

@app.route('/info')
def info():
    return jsonify({'app_name': 'Flask REST API Demo', 'version': '1.0.0'})

@app.route('/status')
def status():
    return jsonify({'status': 'OK', 'uptime': round(time.time() - start_time, 2)})

from flask import request

users = []

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Missing name or email'}), 400
    for user in users:
        if user['email'] == data['email']:
            return jsonify({'error': 'Email already exists'}), 400
    user_id = len(users) + 1
    user = {'id': user_id, 'name': data['name'], 'email': data['email']}
    users.append(user)
    return jsonify({'message': 'User added', 'user': user}), 201

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = next((u for u in users if u['id'] == id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    if 'email' in data:
        if any(u for u in users if u['email'] == data['email'] and u['id'] != id):
            return jsonify({'error': 'Email already taken'}), 400
    user.update({k: v for k, v in data.items() if k in ['name', 'email']})
    return jsonify({'message': 'User updated', 'user': user})

@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    users = [u for u in users if u['id'] != id]
    return jsonify({'message': 'User deleted'}), 200

@app.route('/api/users/clear', methods=['DELETE'])
def clear_users():
    users.clear()
    return jsonify({'message': 'All users cleared'}), 200

@app.route('/api/echo', methods=['POST'])
def echo_json():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    return jsonify({'received': data})

@app.route('/api/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    try:
        a = data.get('a')
        b = data.get('b')
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError
        return jsonify({'product': a * b})
    except:
        return jsonify({'error': 'Invalid input'}), 400
    

    """
    1. Define what a REST API is and list 5 real-world examples. 
    REST (Representational State Transfer) is an architectural style for designing networked applications. A REST API (Application Programming Interface) enables communication between client and server using HTTP methods like GET, POST, PUT, and DELETE. It exposes resources (such as users, posts, products) as URLs and represents data in formats like JSON or XML.
    5 Real-World REST API Examples
| API Name | Purpose | Example Endpoint | 
| GitHub API | Manage repos, users, issues & commits | GET https://api.github.com/repos/{owner}/{repo} | 
| Spotify API | Access music data: tracks, artists, playlists | GET https://api.spotify.com/v1/artists/{id} | 
| OpenWeatherMap API | Retrieve real-time weather data and forecasts | GET https://api.openweathermap.org/data/2.5/weather?q=London | 
| Google Maps API | Location-based services, geocoding, directions | GET https://maps.googleapis.com/maps/api/geocode/json?address=Tokyo | 
| Twilio API | Send SMS, make voice calls, manage communication | POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages.json | 


7. Compare traditional HTML routes vs API JSON responses in your own 
words.
These are typically used in server-side rendered web apps. When you hit a route like /home or /products, the server returns an entire HTML page that browsers can render directly.
API JSON Responses
These are designed purely for data exchange, usually with frontend apps (React, Angular), mobile apps, or other services. Instead of full pages, you return structured data like JSON.
- 📦 Returns raw data (JSON) — readable by software, not humans.
- 🔁 Focuses on functionality, not visuals — loose coupling from UI.
- 🧱 Promotes modular design and reusable endpoints.
- 🚀 Ideal for REST APIs tested with Postman or Thunder Client.
- 🌐 Example:
🔍 Summary of the Difference
| Trait | HTML Route | API JSON Response | 
| Intended audience | Humans via browser | Programs, apps, frontend code | 
| Response format | HTML (with CSS/JS) | JSON (or XML) | 
| Coupling with UI | Tightly coupled | Decoupled | 
| Use case | Web pages | Data exchange via REST endpoints | 

    """