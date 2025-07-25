from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

results = []
student_id_counter = 1

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("name", required=True, help="Name is required")
parser.add_argument("maths", type=int, required=True, help="Maths score is required")
parser.add_argument("science", type=int, required=True, help="Science score is required")
parser.add_argument("english", type=int, required=True, help="English score is required")

# Response helper
def build_response(data=None, message="", status=200):
    return { "message": message, "data": data }, status

# Grade calculator
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

# Resources
class ResultList(Resource):
    def post(self):
        global student_id_counter
        args = parser.parse_args()

        for subject in ["maths", "science", "english"]:
            if args[subject] < 0 or args[subject] > 100:
                return build_response(None, f"{subject.capitalize()} marks must be between 0 and 100", 400)

        total = args["maths"] + args["science"] + args["english"]
        average = round(total / 3, 2)
        grade = calculate_grade(average)

        student = {
            "id": student_id_counter,
            "name": args["name"],
            "maths": args["maths"],
            "science": args["science"],
            "english": args["english"],
            "average": average,
            "grade": grade
        }
        results.append(student)
        student_id_counter += 1
        return build_response(student, "Student result added", 201)

    def get(self):
        return build_response(results, "All student results retrieved")

class Result(Resource):
    def put(self, student_id):
        args = parser.parse_args()

        for subject in ["maths", "science", "english"]:
            if args[subject] < 0 or args[subject] > 100:
                return build_response(None, f"{subject.capitalize()} marks must be between 0 and 100", 400)

        for student in results:
            if student["id"] == student_id:
                total = args["maths"] + args["science"] + args["english"]
                average = round(total / 3, 2)
                grade = calculate_grade(average)

                student.update({
                    "name": args["name"],
                    "maths": args["maths"],
                    "science": args["science"],
                    "english": args["english"],
                    "average": average,
                    "grade": grade
                })
                return build_response(student, "Student result updated")

        return build_response(None, "Student not found", 404)

# Routes
api.add_resource(ResultList, "/results")
api.add_resource(Result, "/results/<int:student_id>")

if __name__ == "__main__":
    app.run(debug=True)