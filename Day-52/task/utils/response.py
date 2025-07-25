# utils/response.py
from flask import jsonify

class ApiResponse:
    @staticmethod
    def success(data, status=200):
        return jsonify({'success': True, 'data': data}), status

    @staticmethod
    def error(message, status=400):
        return jsonify({'success': False, 'error': message}), status