from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import math

app = Flask(__name__)
api = Api(app)

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("amount", type=float, required=True, help="Loan amount is required and must be numeric")
parser.add_argument("interest", type=float, required=True, help="Interest rate is required and must be numeric")
parser.add_argument("years", type=float, required=True, help="Duration (in years) is required and must be numeric")

# EMI calculation helper
def calculate_emi(amount, interest, years):
    monthly_rate = interest / (12 * 100)
    months = years * 12
    emi = amount * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
    return round(emi, 2)

# Response wrapper
def build_response(data=None, message="", status=200):
    return { "message": message, "data": data }, status

# Loan calculator route
class LoanCalculator(Resource):
    def post(self):
        args = parser.parse_args()
        amount = args["amount"]
        interest = args["interest"]
        years = args["years"]

        # Validate positive values
        if amount <= 0 or interest <= 0 or years <= 0:
            return build_response(None, "All values must be greater than zero", 400)

        emi = calculate_emi(amount, interest, years)
        result = {
            "amount": amount,
            "interest_rate": interest,
            "years": years,
            "monthly_emi": emi
        }
        return build_response(result, "EMI calculated", 200)

# Route binding
api.add_resource(LoanCalculator, "/loan/calculate")

if __name__ == "__main__":
    app.run(debug=True)