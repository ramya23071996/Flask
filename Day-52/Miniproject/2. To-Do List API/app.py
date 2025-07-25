from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

tasks = {}  # In-memory storage

task_parser = reqparse.RequestParser()
task_parser.add_argument('title', type=str, required=True, help="Title is required")
task_parser.add_argument('status', type=bool, required=False)

class TaskResource(Resource):
    def get(self, task_id):
        task = tasks.get(task_id)
        if not task:
            return {"message": "Task not found"}, 404
        return task, 200

    def post(self, task_id):
        if task_id in tasks:
            return {"message": "Task already exists"}, 400
        args = task_parser.parse_args()
        tasks[task_id] = {
            "id": task_id,
            "title": args['title'],
            "status": args.get('status', False)
        }
        return tasks[task_id], 201

    def put(self, task_id):
        task = tasks.get(task_id)
        if not task:
            return {"message": "Task not found"}, 404
        args = task_parser.parse_args()
        task["title"] = args['title']
        # Toggle status if provided
        if args['status'] is not None:
            task["status"] = args['status']
        return task, 200

    def delete(self, task_id):
        if task_id not in tasks:
            return {"message": "Task not found"}, 404
        del tasks[task_id]
        return {"message": "Task deleted"}, 204

api.add_resource(TaskResource, '/tasks/<int:task_id>')

@app.errorhandler(500)
def handle_500(error):
    return jsonify({"message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)