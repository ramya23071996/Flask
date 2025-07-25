from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
candidates = {"Alice": 0, "Bob": 0, "Charlie": 0}

@app.route("/")
def index():
    return render_template("index.html", candidates=candidates)

@app.route("/api/vote", methods=["POST"])
def vote():
    data = request.get_json()
    candidate = data.get("candidate")
    if candidate in candidates:
        candidates[candidate] += 1
        return jsonify({"message": "Vote counted!"}), 200
    return jsonify({"error": "Invalid candidate"}), 400

@app.route("/api/results", methods=["GET"])
def results():
    return jsonify(candidates)

if __name__ == "__main__":
    app.run(debug=True)