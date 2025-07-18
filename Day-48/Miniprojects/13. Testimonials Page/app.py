from flask import Flask, render_template

app = Flask(__name__)

@app.route("/testimonials")
def testimonials():
    feedbacks = [
        {
            "name": "Aarav",
            "photo": "user1.jpg",
            "comment": "Fantastic service and support!",
            "rating": 5
        },
        {
            "name": "Meera",
            "photo": "user2.jpg",
            "comment": "Very intuitive and user-friendly.",
            "rating": 4
        },
        {
            "name": "Kiran",
            "photo": "user3.jpg",
            "comment": "Could use a few more features.",
            "rating": 3
        }
    ]
    return render_template("testimonials.html", testimonials=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)