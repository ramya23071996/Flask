from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

contacts = []
contact_id_counter = 1

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("name", required=True, help="Name is required")
parser.add_argument("phone", required=True, help="Phone is required")
parser.add_argument("email", required=True, help="Email is required")

# Response helper
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

# Validator
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

class ContactList(Resource):
    def get(self):
        return build_response(contacts, "Contacts retrieved")

    def post(self):
        global contact_id_counter
        args = parser.parse_args()

        if not is_valid_phone(args["phone"]):
            return build_response(None, "Phone must be 10 digits", 400)

        contact = {
            "id": contact_id_counter,
            "name": args["name"],
            "phone": args["phone"],
            "email": args["email"]
        }
        contacts.append(contact)
        contact_id_counter += 1
        return build_response(contact, "Contact added", 201)

class Contact(Resource):
    def get(self, contact_id):
        for c in contacts:
            if c["id"] == contact_id:
                return build_response(c, "Contact found")
        return build_response(None, "Contact not found", 404)

    def put(self, contact_id):
        args = parser.parse_args()

        if not is_valid_phone(args["phone"]):
            return build_response(None, "Phone must be 10 digits", 400)

        for c in contacts:
            if c["id"] == contact_id:
                c.update({
                    "name": args["name"],
                    "phone": args["phone"],
                    "email": args["email"]
                })
                return build_response(c, "Contact updated")
        return build_response(None, "Contact not found", 404)

    def delete(self, contact_id):
        global contacts
        for c in contacts:
            if c["id"] == contact_id:
                contacts = [ct for ct in contacts if ct["id"] != contact_id]
                return build_response(None, "Contact deleted", 200)
        return build_response(None, "Contact not found", 404)

# Routes
api.add_resource(ContactList, "/contacts")
api.add_resource(Contact, "/contacts/<int:contact_id>")

if __name__ == "__main__":
    app.run(debug=True)