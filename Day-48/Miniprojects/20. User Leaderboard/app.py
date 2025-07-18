from flask import Flask, render_template

app = Flask(__name__)

@app.route("/leaderboard")
def leaderboard():
    users = [
        {"name": "Ramya", "score": 980},
        {"name": "Arjun", "score": 920},
        {"name": "Diya", "score": 890}
    ]
    return render_template("leaderboard.html", leaderboard=users)

if __name__ == "__main__":
    app.run(debug=True)