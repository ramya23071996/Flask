# resources/user.py
from flask_restful import Resource
from flask import request
from utils.response import ApiResponse

users = []

class UserListResource(Resource):
    def get(self):
        return ApiResponse.success(users)
    
    def post(self):
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return ApiResponse.error('Missing fields', 400)
        user_id = len(users) + 1
        user = {'id': user_id, 'name': data['name'], 'email': data['email']}
        users.append(user)
        return ApiResponse.success(user, 201)

class UserResource(Resource):
    def get(self, user_id):
        user = next((u for u in users if u['id'] == user_id), None)
        if not user:
            return ApiResponse.error('Not found', 404)
        return ApiResponse.success(user)

# api_app.py (register RESTful)
from flask_restful import Api
from resources.user import UserListResource, UserResource

api = Api(app)
api.add_resource(UserListResource, '/api/users')
api.add_resource(UserResource, '/api/users/<int:user_id>')