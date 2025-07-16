from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# Sample book database
book_db = [
    {'title': 'Dune', 'genre': 'sci-fi'},
    {'title': 'Neuromancer', 'genre': 'sci-fi'},
    {'title': 'Pride and Prejudice', 'genre': 'romance'},
    {'title': 'The Notebook', 'genre': 'romance'},
    {'title': 'Foundation', 'genre': 'sci-fi'},
    {'title': 'Me Before You', 'genre': 'romance'}
]

# In-memory recommendation log
recommendations = []

# 1. /recommend – form to choose genre
@app.route('/recommend', methods=['GET'])
def recommend_form():
    return '''
    <h2>Get a Book Recommendation</h2>
    <form method="POST" action="/show-recommendation">
        Your Name: <input type="text" name="user"><br>
        Genre:
        <select name="genre">
            <option value="sci-fi">Sci-Fi</option>
            <option value="romance">Romance</option>
        </select><br>
        <input type="submit" value="Recommend Me">
    </form>
    '''

# 2. /show-recommendation – handle POST and redirect
@app.route('/show-recommendation', methods=['POST'])
def show_recommendation():
    user = request.form.get('user', 'Reader').strip()
    genre = request.form.get('genre', '').strip().lower()

    # Store recommendation request
    recommendations.append({'user': user, 'genre': genre})

    return redirect(url_for('thank_user', user=user))

# 3. /thanks/<user> – personalized thank-you
@app.route('/thanks/<user>')
def thank_user(user):
    return f"<h3>Thanks, {escape(user)}! We hope you enjoy your recommended books.</h3>"

# 4. /books?genre=sci-fi – filter books by genre
@app.route('/books')
def books_by_genre():
    genre = request.args.get('genre', '').strip().lower()
    filtered = [b for b in book_db if b['genre'] == genre]

    if not filtered:
        return f"<p>No books found for genre: {escape(genre)}</p>"

    items = "".join([
        f"<li><a href='/book/{escape(b['title'])}'>{escape(b['title'])}</a></li>"
        for b in filtered
    ])
    return f"<h3>Books in {escape(genre.capitalize())}</h3><ul>{items}</ul>"

# 5. /book/<title> – dynamic book detail route
@app.route('/book/<title>')
def book_detail(title):
    match = next((b for b in book_db if b['title'].lower() == title.lower()), None)
    if match:
        return f"""
        <h3>{escape(match['title'])}</h3>
        <p>Genre: {escape(match['genre'].capitalize())}</p>
        <p>This is a recommended read for fans of {escape(match['genre'])} fiction.</p>
        """
    return f"<p>Book titled '{escape(title)}' not found.</p>"

if __name__ == '__main__':
    app.run(debug=True)