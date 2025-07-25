from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

issues = []
issue_id_counter = 1
VALID_STATUS = {"open", "closed"}

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("title", required=True, help="Title is required")
parser.add_argument("description", required=True, help="Description is required")
parser.add_argument("status", required=True, help="Status is required (open/closed)")

# Helper for responses
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

def is_valid_status(value):
    return value.lower() in VALID_STATUS

class IssueList(Resource):
    def get(self):
        return build_response(issues, "All issues retrieved")

    def post(self):
        global issue_id_counter
        args = parser.parse_args()

        if not is_valid_status(args["status"]):
            return build_response(None, "Invalid status. Must be 'open' or 'closed'", 400)

        issue = {
            "id": issue_id_counter,
            "title": args["title"],
            "description": args["description"],
            "status": args["status"].lower()
        }
        issues.append(issue)
        issue_id_counter += 1
        return build_response(issue, "Issue reported", 201)

class Issue(Resource):
    def get(self, issue_id):
        for i in issues:
            if i["id"] == issue_id:
                return build_response(i, "Issue found")
        return build_response(None, "Issue not found", 404)

    def put(self, issue_id):
        args = parser.parse_args()

        if not is_valid_status(args["status"]):
            return build_response(None, "Invalid status. Must be 'open' or 'closed'", 400)

        for i in issues:
            if i["id"] == issue_id:
                i.update({
                    "title": args["title"],
                    "description": args["description"],
                    "status": args["status"].lower()
                })
                msg = "Issue updated" if i["status"] == "open" else "Issue marked as resolved"
                return build_response(i, msg)
        return build_response(None, "Issue not found", 404)

    def delete(self, issue_id):
        global issues
        for i in issues:
            if i["id"] == issue_id:
                issues = [iss for iss in issues if iss["id"] != issue_id]
                return build_response(None, "Issue deleted", 200)
        return build_response(None, "Issue not found", 404)

# Routing
api.add_resource(IssueList, "/issues")
api.add_resource(Issue, "/issues/<int:issue_id>")

if __name__ == "__main__":
    app.run(debug=True)