from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import re

app = Flask(__name__)
api = Api(app)

feedbacks = []

# Email regex validator
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("name", required=True, help="Name is required")
parser.add_argument("email", required=True, help="Email is required")
parser.add_argument("message", required=True, help="Message is required")

# Response helper
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

class Feedback(Resource):
    def post(self):
        args = parser.parse_args()
        email = args["email"]

        if not re.match(EMAIL_REGEX, email):
            return build_response(None, "Invalid email format", 400)

        entry = {
            "id": len(feedbacks) + 1,
            "name": args["name"],
            "email": email,
            "message": args["message"]
        }

        feedbacks.append(entry)
        return build_response(entry, f"Thank you for your feedback, {args['name']}!", 201)

# Route
api.add_resource(Feedback, "/feedback")

if __name__ == "__main__":
    app.run(debug=True)