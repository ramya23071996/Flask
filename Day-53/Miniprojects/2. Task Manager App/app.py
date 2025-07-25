from flask import Flask, jsonify, request, render_template
from tasks_data import tasks

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.json
    if "title" not in data or not data["title"].strip():
        return jsonify({"error": "Task title is required"}), 400
    task = {"id": len(tasks) + 1, "title": data["title"]}
    tasks.append(task)
    return jsonify(task), 201

if __name__ == "__main__":
    app.run(debug=True)