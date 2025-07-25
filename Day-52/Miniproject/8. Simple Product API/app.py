from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

products = []
product_id_counter = 1

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("name", required=True, help="Name is required")
parser.add_argument("price", type=float, required=True, help="Price must be a number")
parser.add_argument("in_stock", type=bool, required=True, help="In_stock is required and must be true/false")

# Response helper
def build_response(data=None, message="", status=200):
    return {"message": message, "data": data}, status

class ProductList(Resource):
    def post(self):
        global product_id_counter
        args = parser.parse_args()
        
        if args["price"] <= 0:
            return build_response(None, "Price must be greater than 0", 400)

        product = {
            "id": product_id_counter,
            "name": args["name"],
            "price": args["price"],
            "in_stock": args["in_stock"]
        }
        products.append(product)
        product_id_counter += 1
        return build_response(product, "Product added", 201)

    def get(self):
        return build_response(products, "Products retrieved")

class Product(Resource):
    def put(self, product_id):
        args = parser.parse_args()
        
        if args["price"] <= 0:
            return build_response(None, "Price must be greater than 0", 400)

        for p in products:
            if p["id"] == product_id:
                p.update({
                    "name": args["name"],
                    "price": args["price"],
                    "in_stock": args["in_stock"]
                })
                return build_response(p, "Product updated")
        return build_response(None, "Product not found", 404)

    def delete(self, product_id):
        global products
        for p in products:
            if p["id"] == product_id:
                products = [prod for prod in products if prod["id"] != product_id]
                return build_response(None, "Product deleted", 200)
        return build_response(None, "Product not found", 404)

# Routes
api.add_resource(ProductList, "/products")
api.add_resource(Product, "/products/<int:product_id>")

if __name__ == "__main__":
    app.run(debug=True)