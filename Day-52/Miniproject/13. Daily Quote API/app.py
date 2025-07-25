from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

quotes = []
quote_id_counter = 1

# Parser
parser = reqparse.RequestParser()
parser.add_argument("text", required=True, help="Quote text is required")

# Response builder
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

# Resource to handle list and create
class QuoteList(Resource):
    def get(self):
        return build_response(quotes, "All quotes retrieved")

    def post(self):
        global quote_id_counter
        args = parser.parse_args()
        quote = {
            "id": quote_id_counter,
            "text": args["text"]
        }
        quotes.append(quote)
        quote_id_counter += 1
        return build_response(quote, "Quote added", 201)

# Resource to handle single quote updates and deletion
class Quote(Resource):
    def put(self, quote_id):
        args = parser.parse_args()
        for q in quotes:
            if q["id"] == quote_id:
                q["text"] = args["text"]
                return build_response(q, "Quote updated")
        return build_response(None, "Quote not found", 404)

    def delete(self, quote_id):
        global quotes
        for q in quotes:
            if q["id"] == quote_id:
                quotes = [qt for qt in quotes if qt["id"] != quote_id]
                return build_response(None, "Quote deleted", 200)
        return build_response(None, "Quote not found", 404)

# Resource for random selection
class RandomQuote(Resource):
    def get(self):
        if not quotes:
            return build_response(None, "No inspirational quotes available", 404)
        quote = random.choice(quotes)
        return build_response(quote, "Here’s your quote of the day!")

# Routes
api.add_resource(QuoteList, "/quotes")
api.add_resource(Quote, "/quotes/<int:quote_id>")
api.add_resource(RandomQuote, "/quote/random")

if __name__ == "__main__":
    app.run(debug=True)