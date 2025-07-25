from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

user_profile = {
    "id": 1,
    "name": "Ramya",
    "email": "ramya.dev@example.com",
    "location": "Coimbatore"
}

@app.route('/')
def index():
    return render_template('profile.html', user=user_profile)

@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if user_id == user_profile['id']:
        user_profile.update(data)
        return jsonify({"status": "success", "user": user_profile})
    return jsonify({"status": "error", "msg": "User not found"}), 404