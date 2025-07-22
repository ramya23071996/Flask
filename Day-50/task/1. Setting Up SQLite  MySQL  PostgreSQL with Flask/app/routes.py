from flask import request, jsonify
from . import db
from .models import Complaint

def register_routes(app):
    @app.route("/submit", methods=["POST"])
    def submit_complaint():
        data = request.json
        try:
            complaint = Complaint(
                user_name=data["user_name"],
                email=data["email"],
                complaint_text=data["complaint_text"]
            )
            db.session.add(complaint)
            db.session.commit()
            return jsonify({"message": "Complaint submitted!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500