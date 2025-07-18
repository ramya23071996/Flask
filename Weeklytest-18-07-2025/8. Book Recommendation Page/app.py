from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample book recommendations by genre
book_data = {
    "fantasy": ["Harry Potter", "The Hobbit", "The Name of the Wind"],
    "sci-fi": ["Dune", "Ender's Game", "Neuromancer"],
    "mystery": ["Gone Girl", "Sherlock Holmes", "The Girl with the Dragon Tattoo"],
    "romance": ["Pride and Prejudice", "The Notebook", "Me Before You"]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        genre = request.form.get('genre').lower()
        return redirect(url_for('books', genre=genre))
    return render_template('index.html')

@app.route('/books/<genre>')
def books(genre):
    recommended_books = book_data.get(genre, [])
    return render_template('books.html', genre=genre, books=recommended_books)

if __name__ == '__main__':
    app.run(debug=True)
