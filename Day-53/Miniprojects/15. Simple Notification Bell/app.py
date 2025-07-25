from flask import Flask, jsonify, render_template

app = Flask(__name__)

notifications = [
    {"id": 1, "message": "New comment on your post", "read": False},
    {"id": 2, "message": "New follower: Ananya", "read": False},
    {"id": 3, "message": "System update scheduled", "read": True}
]

@app.route('/')
def index():
    return render_template('bell.html')

@app.route('/api/notifications')
def get_notifications():
    unread = [n for n in notifications if not n["read"]]
    return jsonify({
        "unread_count": len(unread),
        "notifications": unread
    })