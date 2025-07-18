from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded movie data by genre
movie_data = {
    "action": ["Mad Max: Fury Road", "John Wick", "Gladiator"],
    "comedy": ["Superbad", "Step Brothers", "The Mask"],
    "drama": ["Forrest Gump", "The Shawshank Redemption", "The Godfather"],
    "sci-fi": ["Inception", "Interstellar", "The Matrix"]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        genre = request.form.get('genre')
        return redirect(url_for('movies', genre=genre))
    genres = list(movie_data.keys())
    return render_template('index.html', genres=genres)

@app.route('/movies/<genre>')
def movies(genre):
    movies = movie_data.get(genre.lower(), [])
    return render_template('movies.html', genre=genre.title(), movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
