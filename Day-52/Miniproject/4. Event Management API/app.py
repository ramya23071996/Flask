from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from datetime import datetime

app = Flask(__name__)
api = Api(app)

events = {}  # In-memory mock DB

# Parser for input validation
event_parser = reqparse.RequestParser()
event_parser.add_argument('name', type=str, required=True, help="Event name is required")
event_parser.add_argument('date', type=str, required=True, help="Event date is required (YYYY-MM-DD)")
event_parser.add_argument('location', type=str, required=False)

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class EventResource(Resource):
    def get(self, event_id):
        event = events.get(event_id)
        if not event:
            return {"message": "Event not found"}, 404
        return event, 200

    def post(self, event_id):
        if event_id in events:
            return {"message": "Event already exists"}, 400
        args = event_parser.parse_args()
        if not validate_date(args['date']):
            return {"message": "Invalid date format. Use YYYY-MM-DD."}, 400
        events[event_id] = {
            "id": event_id,
            "name": args['name'],
            "date": args['date'],
            "location": args.get('location', "")
        }
        return events[event_id], 201

    def put(self, event_id):
        event = events.get(event_id)
        if not event:
            return {"message": "Event not found"}, 404
        args = event_parser.parse_args()
        if not validate_date(args['date']):
            return {"message": "Invalid date format. Use YYYY-MM-DD."}, 400
        event["name"] = args['name']
        event["date"] = args['date']
        event["location"] = args.get('location', event["location"])
        return event, 200

    def delete(self, event_id):
        if event_id not in events:
            return {"message": "Event not found"}, 404
        del events[event_id]
        return {"message": "Event deleted"}, 204

# Register routes
api.add_resource(EventResource, '/events/<int:event_id>')

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)