from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

books = [
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "year": "2018",
        "summary": "Tiny changes, remarkable results. A guide to building better habits."
    },
    {
        "title": "Deep Work",
        "author": "Cal Newport",
        "year": "2016",
        "summary": "Rules for focused success in a distracted world."
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "Andy Hunt & Dave Thomas",
        "year": "1999",
        "summary": "Classic tips for becoming a better, adaptable software engineer."
    },
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": "2008",
        "summary": "A handbook of agile software craftsmanship."
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/book/suggest", methods=["GET"])
def suggest_book():
    book = random.choice(books)
    return jsonify(book)

if __name__ == "__main__":
    app.run(debug=True)