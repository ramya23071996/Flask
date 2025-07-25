from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import re

app = Flask(__name__)
api = Api(app)

subscriptions = []

# Simple email regex
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

# Parser for subscription
parser = reqparse.RequestParser()
parser.add_argument("email", required=True, help="Email is required")

# Response builder
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

class Subscribe(Resource):
    def post(self):
        args = parser.parse_args()
        email = args["email"]

        if not re.match(EMAIL_REGEX, email):
            return build_response(None, "Invalid email format", 400)

        if email in subscriptions:
            return build_response(None, "Email is already subscribed", 400)

        subscriptions.append(email)
        return build_response({"email": email}, "Subscription successful", 201)

class Unsubscribe(Resource):
    def delete(self, email):
        if not re.match(EMAIL_REGEX, email):
            return build_response(None, "Invalid email format", 400)

        if email not in subscriptions:
            return build_response(None, "Email not found in subscription list", 404)

        subscriptions.remove(email)
        return build_response({"email": email}, "Unsubscribed successfully", 200)

# Routes
api.add_resource(Subscribe, "/subscribe")
api.add_resource(Unsubscribe, "/subscribe/<string:email>")

if __name__ == "__main__":
    app.run(debug=True)