from flask import Flask, render_template

app = Flask(__name__)

@app.route("/team")
def team():
    team_members = [
        {"name": "Alice", "role": "Team Lead", "photo": "alice.jpg"},
        {"name": "Bob", "role": "Frontend Developer", "photo": "bob.jpg"},
        {"name": "Carol", "role": "Backend Developer", "photo": "carol.jpg"}
    ]
    return render_template("team.html", team=team_members)

if __name__ == "__main__":
    app.run(debug=True)