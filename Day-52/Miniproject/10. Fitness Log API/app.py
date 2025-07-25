from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

workouts = []
workout_id_counter = 1

# Parser
parser = reqparse.RequestParser()
parser.add_argument("user", required=True, help="User name is required")
parser.add_argument("type", required=True, help="Workout type is required")
parser.add_argument("duration", type=int, required=True, help="Duration must be an integer")

# Response builder
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

# Resources
class WorkoutList(Resource):
    def get(self):
        return build_response(workouts, "All workouts retrieved")

    def post(self):
        global workout_id_counter
        args = parser.parse_args()

        if args["duration"] <= 0:
            return build_response(None, "Duration must be greater than 0", 400)

        workout = {
            "id": workout_id_counter,
            "user": args["user"],
            "type": args["type"],
            "duration": args["duration"]
        }
        workouts.append(workout)
        workout_id_counter += 1
        return build_response(workout, "Workout added", 201)

class Workout(Resource):
    def put(self, workout_id):
        args = parser.parse_args()

        if args["duration"] <= 0:
            return build_response(None, "Duration must be greater than 0", 400)

        for w in workouts:
            if w["id"] == workout_id:
                w.update({
                    "user": args["user"],
                    "type": args["type"],
                    "duration": args["duration"]
                })
                return build_response(w, "Workout updated")
        return build_response(None, "Workout not found", 404)

    def delete(self, workout_id):
        global workouts
        for w in workouts:
            if w["id"] == workout_id:
                workouts = [wk for wk in workouts if wk["id"] != workout_id]
                return build_response(None, "Workout deleted", 200)
        return build_response(None, "Workout not found", 404)

class WorkoutSummary(Resource):
    def get(self):
        total = sum(w["duration"] for w in workouts)
        return build_response({"total_duration": total}, "Workout summary")

# Routes
api.add_resource(WorkoutList, "/workouts")
api.add_resource(Workout, "/workouts/<int:workout_id>")
api.add_resource(WorkoutSummary, "/summary")

if __name__ == "__main__":
    app.run(debug=True)