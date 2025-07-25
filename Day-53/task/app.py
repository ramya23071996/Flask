from flask import Flask, render_template, jsonify, request, make_response
import random, time
from data import USERS, PRODUCTS, MESSAGES, APP_VERSION
from utils import get_uptime, paginate, error_response

app = Flask(__name__)
APP_START_TIME = time.time()

@app.route("/")
def index():
    return render_template("index.html", users=USERS, user_id=USERS[0]["id"])

@app.route("/api/time")
def time_api():
    return jsonify({"time": time.strftime("%Y-%m-%d %H:%M:%S")})

@app.route("/api/status")
def status_api():
    return jsonify({
        "status": "running",
        "uptime": get_uptime(APP_START_TIME),
        "app_version": APP_VERSION
    })

@app.route("/api/users")
def users_api():
    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=5, type=int)
    return jsonify({
        "users": paginate(USERS, page, limit),
        "page": page,
        "limit": limit
    })

@app.route("/api/random")
def random_api():
    return jsonify({"message": random.choice(MESSAGES)})

@app.route("/api/products")
def products_api():
    return jsonify({"products": PRODUCTS})

@app.route("/api/greet")
def greet_api():
    name = request.args.get("name")
    if not name:
        return error_response("Name is required", 400)
    return jsonify({"greeting": f"Hello, {name}!"})

@app.route("/api/submit", methods=["POST"])
def submit_api():
    data = request.json or {}
    msg = data.get("message", "")
    return jsonify({"response": f"Received: {msg}"})

@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json or {}
    return jsonify({"updated_user": {"id": user_id, "new_data": data}})

@app.route("/api/search")
def search_api():
    query = request.args.get("q", "")
    results = [u for u in USERS if query.lower() in u["name"].lower()]
    return jsonify({"results": results})

@app.route("/api/custom-header")
def custom_header():
    response = make_response(jsonify({"status": "Header attached"}))
    response.headers["X-Custom-Header"] = "Ramya-Rocks 🚀"
    return response