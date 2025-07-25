from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

tickets = []
ticket_id_counter = 1

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("email", required=True, help="Email is required")
parser.add_argument("issue", required=True, help="Issue description is required")
parser.add_argument("priority", required=True, help="Priority is required")

# Response helper
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

class TicketList(Resource):
    def get(self):
        return build_response(tickets, "All tickets retrieved")

    def post(self):
        global ticket_id_counter
        args = parser.parse_args()

        ticket = {
            "id": ticket_id_counter,
            "email": args["email"],
            "issue": args["issue"],
            "priority": args["priority"],
            "status": "Open"
        }
        tickets.append(ticket)
        ticket_id_counter += 1
        return build_response(ticket, "Ticket submitted", 201)

class Ticket(Resource):
    def put(self, ticket_id):
        for t in tickets:
            if t["id"] == ticket_id:
                t["status"] = "Resolved"
                return build_response(t, "Ticket closed")
        return build_response(None, "Ticket not found", 404)

    def delete(self, ticket_id):
        global tickets
        for t in tickets:
            if t["id"] == ticket_id:
                tickets = [tick for tick in tickets if tick["id"] != ticket_id]
                return build_response(None, "Ticket deleted", 200)
        return build_response(None, "Ticket not found", 404)

# Routes
api.add_resource(TicketList, "/tickets")
api.add_resource(Ticket, "/tickets/<int:ticket_id>")

if __name__ == "__main__":
    app.run(debug=True)