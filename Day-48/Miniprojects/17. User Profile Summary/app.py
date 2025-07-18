from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

# Sample user data
users = {
    "ramya": {
        "name": "Ramya",
        "bio": "Full stack developer and UI/UX enthusiast.",
        "joined": datetime(2025, 7, 10),
        "image": "ramya.jpg"
    },
    "arjun": {
        "name": "Arjun",
        "bio": "Data analyst with a passion for visualization.",
        "joined": datetime(2025, 6, 1),
        "image": "arjun.jpg"
    },
    "diya": {
        "name": "Diya",
        "bio": "New to the platform, exploring tech and design.",
        "joined": datetime(2025, 7, 17),
        "image": "diya.jpg"
    }
}

@app.route("/profile/<username>")
def profile(username):
    user = users.get(username)
    if not user:
        return "User not found", 404
    days_since_joined = (datetime.now() - user["joined"]).days
    is_new = days_since_joined < 7
    return render_template("profile.html", user=user, is_new=is_new)

if __name__ == "__main__":
    app.run(debug=True)