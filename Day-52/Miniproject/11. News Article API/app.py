from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from datetime import datetime

app = Flask(__name__)
api = Api(app)

articles = []
article_id_counter = 1

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("headline", required=True, help="Headline is required")
parser.add_argument("category", required=True, help="Category is required")
parser.add_argument("published_date", required=True, help="Published date is required in YYYY-MM-DD format")

# Response helper
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

# Article list and creation
class ArticleList(Resource):
    def get(self):
        category = request.args.get("category")
        date = request.args.get("date")

        result = articles
        if category:
            result = [a for a in result if a["category"].lower() == category.lower()]
        if date:
            result = [a for a in result if a["published_date"] == date]

        return build_response(result, "Articles retrieved")

    def post(self):
        global article_id_counter
        args = parser.parse_args()

        # Validate date format
        try:
            datetime.strptime(args["published_date"], "%Y-%m-%d")
        except ValueError:
            return build_response(None, "Invalid date format. Use YYYY-MM-DD", 400)

        article = {
            "id": article_id_counter,
            "headline": args["headline"],
            "category": args["category"],
            "published_date": args["published_date"]
        }
        articles.append(article)
        article_id_counter += 1
        return build_response(article, "Article added", 201)

# Single article operations
class Article(Resource):
    def get(self, article_id):
        for a in articles:
            if a["id"] == article_id:
                return build_response(a, "Article found")
        return build_response(None, "Article not found", 404)

    def put(self, article_id):
        args = parser.parse_args()
        for a in articles:
            if a["id"] == article_id:
                a.update({
                    "headline": args["headline"],
                    "category": args["category"],
                    "published_date": args["published_date"]
                })
                return build_response(a, "Article updated")
        return build_response(None, "Article not found", 404)

    def delete(self, article_id):
        global articles
        for a in articles:
            if a["id"] == article_id:
                articles = [art for art in articles if art["id"] != article_id]
                return build_response(None, "Article deleted", 200)
        return build_response(None, "Article not found", 404)

# Routes
api.add_resource(ArticleList, "/articles")
api.add_resource(Article, "/articles/<int:article_id>")

if __name__ == "__main__":
    app.run(debug=True)