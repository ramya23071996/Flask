from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# In-memory book store
books = []
book_id_counter = 1

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("title", required=True, help="Title is required")
parser.add_argument("author", required=True, help="Author is required")
parser.add_argument("year", type=int, required=True, help="Year is required")

# Response helper
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

# Resource classes
class BookList(Resource):
    def get(self):
        author = request.args.get("author")
        filtered = [b for b in books if b["author"] == author] if author else books
        return build_response(filtered, "Books retrieved")

    def post(self):
        global book_id_counter
        args = parser.parse_args()
        book = {
            "id": book_id_counter,
            "title": args["title"],
            "author": args["author"],
            "year": args["year"]
        }
        books.append(book)
        book_id_counter += 1
        return build_response(book, "Book added", 201)

class Book(Resource):
    def get(self, book_id):
        for b in books:
            if b["id"] == book_id:
                return build_response(b, "Book found")
        return build_response(None, "Book not found", 404)

    def put(self, book_id):
        args = parser.parse_args()
        for b in books:
            if b["id"] == book_id:
                b.update(args)
                return build_response(b, "Book updated")
        return build_response(None, "Book not found", 404)

    def delete(self, book_id):
        global books
        books = [b for b in books if b["id"] != book_id]
        return build_response(None, "Book deleted")

# Routing
api.add_resource(BookList, "/books")
api.add_resource(Book, "/books/<int:book_id>")

if __name__ == "__main__":
    app.run(debug=True)