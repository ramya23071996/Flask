from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

users = {}  # Simulated in-memory database

class UserResource(Resource):
    def get(self, user_id):
        user = users.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return user, 200

    def post(self, user_id):
        if user_id in users:
            return {"message": "User already exists"}, 400
        data = request.get_json()
        users[user_id] = {
            "id": user_id,
            "name": data.get("name", ""),
            "email": data.get("email", "")
        }
        return users[user_id], 201

    def put(self, user_id):
        data = request.get_json()
        user = users.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        user["name"] = data.get("name", user["name"])
        user["email"] = data.get("email", user["email"])
        return user, 200

    def delete(self, user_id):
        if user_id not in users:
            return {"message": "User not found"}, 404
        del users[user_id]
        return {"message": "User deleted"}, 204

api.add_resource(UserResource, '/users/<int:user_id>')

# Custom error handler example
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)