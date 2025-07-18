from flask import Flask, render_template

app = Flask(__name__)

@app.route("/movies")
def movies():
    movie_list = [
        {
            "title": "Inception",
            "poster": "movie1.jpg",
            "rating": 5,
            "new_release": False
        },
        {
            "title": "Oppenheimer",
            "poster": "movie2.jpg",
            "rating": 4,
            "new_release": True
        },
        {
            "title": "Interstellar",
            "poster": "movie3.jpg",
            "rating": 5,
            "new_release": False
        }
    ]
    return render_template("movies.html", movies=movie_list)

if __name__ == "__main__":
    app.run(debug=True)