from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory rating log
ratings = []

# 1. /rate – form to submit movie rating
@app.route('/rate', methods=['GET'])
def rate_form():
    return '''
    <h2>Rate a Movie</h2>
    <form method="POST" action="/submit-rating">
        Your Name: <input type="text" name="name"><br>
        Movie Title: <input type="text" name="movie"><br>
        Rating (1–10): <input type="number" name="rating" min="1" max="10"><br>
        <input type="submit" value="Submit Rating">
    </form>
    '''

# 2. /submit-rating – handle POST and redirect
@app.route('/submit-rating', methods=['POST'])
def submit_rating():
    name = request.form.get('name', 'Anonymous').strip()
    movie = request.form.get('movie', '').strip()
    rating = request.form.get('rating', '0').strip()

    # Store rating
    ratings.append({
        'name': name,
        'movie': movie,
        'rating': int(rating)
    })

    # Redirect to thank-you page
    return redirect(url_for('thank_you', name=name))

# 3. /thank-you/<name> – personalized thank-you
@app.route('/thank-you/<name>')
def thank_you(name):
    return f"<h3>Thank you, {escape(name)}! Your rating has been recorded.</h3>"

# 4. /ratings?movie=Inception – filter ratings by movie
@app.route('/ratings')
def ratings_by_movie():
    movie = request.args.get('movie', '').strip().lower()
    filtered = [r for r in ratings if r['movie'].lower() == movie] if movie else ratings

    if not filtered:
        return f"<p>No ratings found for movie: {escape(movie.title())}</p>"

    items = "".join([
        f"<li>{escape(r['name'])} rated <strong>{escape(r['movie'])}</strong>: {r['rating']}/10</li>"
        for r in filtered
    ])
    return f"<h3>Ratings for {escape(movie.title())}</h3><ul>{items}</ul>"

# 5. /movie/<title> – dynamic movie info
@app.route('/movie/<title>')
def movie_info(title):
    title_lower = title.lower()
    movie_ratings = [r for r in ratings if r['movie'].lower() == title_lower]

    if not movie_ratings:
        return f"<p>No information available for movie: {escape(title)}</p>"

    avg_rating = sum(r['rating'] for r in movie_ratings) / len(movie_ratings)
    items = "".join([
        f"<li>{escape(r['name'])} – {r['rating']}/10</li>"
        for r in movie_ratings
    ])
    return f"""
    <h3>Movie: {escape(title.title())}</h3>
    <p>Average Rating: {avg_rating:.1f}/10</p>
    <ul>{items}</ul>
    """

if __name__ == '__main__':
    app.run(debug=True)