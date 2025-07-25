from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

students = []
student_id_counter = 1

# Allowed grades
VALID_GRADES = {"A", "B", "C", "D"}

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("name", required=True, help="Name is required")
parser.add_argument("roll", required=True, help="Roll number is required")
parser.add_argument("grade", required=True, help="Grade is required")

# Response helper
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

class StudentList(Resource):
    def post(self):
        global student_id_counter
        args = parser.parse_args()
        if args["grade"].upper() not in VALID_GRADES:
            return build_response(None, "Invalid grade. Must be A, B, C, or D", 400)

        student = {
            "id": student_id_counter,
            "name": args["name"],
            "roll": args["roll"],
            "grade": args["grade"].upper()
        }
        students.append(student)
        student_id_counter += 1
        return build_response(student, "Student added", 201)

class Student(Resource):
    def put(self, student_id):
        args = parser.parse_args()
        if args["grade"].upper() not in VALID_GRADES:
            return build_response(None, "Invalid grade. Must be A, B, C, or D", 400)

        for s in students:
            if s["id"] == student_id:
                s.update({
                    "name": args["name"],
                    "roll": args["roll"],
                    "grade": args["grade"].upper()
                })
                return build_response(s, "Student updated")
        return build_response(None, "Student not found", 404)

    def delete(self, student_id):
        global students
        for s in students:
            if s["id"] == student_id:
                students = [stu for stu in students if stu["id"] != student_id]
                return build_response(None, "Student deleted", 200)
        return build_response(None, "Student not found", 404)

# Routes
api.add_resource(StudentList, "/students")
api.add_resource(Student, "/students/<int:student_id>")

if __name__ == "__main__":
    app.run(debug=True)