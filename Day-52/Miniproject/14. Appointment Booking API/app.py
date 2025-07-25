from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from datetime import datetime

app = Flask(__name__)
api = Api(app)

appointments = []
appointment_id_counter = 1

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("name", required=True, help="Name is required")
parser.add_argument("date", required=True, help="Date is required")
parser.add_argument("service", required=True, help="Service is required")

# Validate date format
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Response helper
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

class AppointmentList(Resource):
    def get(self):
        return build_response(appointments, "All appointments retrieved")

    def post(self):
        global appointment_id_counter
        args = parser.parse_args()

        if not is_valid_date(args["date"]):
            return build_response(None, "Date must be in YYYY-MM-DD format", 400)

        appointment = {
            "id": appointment_id_counter,
            "name": args["name"],
            "date": args["date"],
            "service": args["service"]
        }
        appointments.append(appointment)
        appointment_id_counter += 1
        return build_response(appointment, f"Appointment booked for {args['name']}!", 201)

class Appointment(Resource):
    def put(self, appointment_id):
        args = parser.parse_args()

        if not is_valid_date(args["date"]):
            return build_response(None, "Date must be in YYYY-MM-DD format", 400)

        for a in appointments:
            if a["id"] == appointment_id:
                a.update({
                    "name": args["name"],
                    "date": args["date"],
                    "service": args["service"]
                })
                return build_response(a, "Appointment updated")
        return build_response(None, "Appointment not found", 404)

    def delete(self, appointment_id):
        global appointments
        for a in appointments:
            if a["id"] == appointment_id:
                appointments = [appt for appt in appointments if appt["id"] != appointment_id]
                return build_response(None, "Appointment cancelled", 200)
        return build_response(None, "Appointment not found", 404)

# Routes
api.add_resource(AppointmentList, "/appointments")
api.add_resource(Appointment, "/appointments/<int:appointment_id>")

if __name__ == "__main__":
    app.run(debug=True)