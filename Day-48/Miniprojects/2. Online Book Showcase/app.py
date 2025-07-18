from flask import Flask, render_template

app = Flask(__name__)

# Sample book data
books = [
    {"name": "The Pragmatic Programmer", "author": "Andrew Hunt", "cover": "book1.jpg"},
    {"name": "Clean Code", "author": "Robert C. Martin", "cover": "book2.jpg"},
    {"name": "Fluent Python", "author": "Luciano Ramalho", "cover": "book3.jpg"},
]

@app.route("/books")
def show_books():
    return render_template("books.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)