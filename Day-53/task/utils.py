import time
from flask import jsonify

def get_uptime(start):
    return f"{time.time() - start:.2f} seconds"

def paginate(data, page, limit):
    offset = (page - 1) * limit
    return data[offset:offset+limit]

def error_response(msg, code):
    response = jsonify({"error": msg})
    response.status_code = code
    return response