from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

cart_items = []
item_id_counter = 1

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("product_name", required=True, help="Product name is required")
parser.add_argument("quantity", type=int, required=True, help="Quantity is required and must be an integer")
parser.add_argument("price", type=float, required=True, help="Price is required and must be a number")

# Response builder
def build_response(data=None, message="", status=200):
    return { "message": message, "data": data }, status

# Resources
class Cart(Resource):
    def get(self):
        return build_response(cart_items, "Cart retrieved")

    def post(self):
        global item_id_counter
        args = parser.parse_args()

        if args["quantity"] <= 0:
            return build_response(None, "Quantity must be greater than 0", 400)
        if args["price"] <= 0:
            return build_response(None, "Price must be greater than 0", 400)

        item = {
            "id": item_id_counter,
            "product_name": args["product_name"],
            "quantity": args["quantity"],
            "price": args["price"]
        }
        cart_items.append(item)
        item_id_counter += 1
        return build_response(item, "Item added to cart", 201)

class CartItem(Resource):
    def put(self, item_id):
        args = parser.parse_args()

        if args["quantity"] <= 0:
            return build_response(None, "Quantity must be greater than 0", 400)
        if args["price"] <= 0:
            return build_response(None, "Price must be greater than 0", 400)

        for item in cart_items:
            if item["id"] == item_id:
                item.update({
                    "product_name": args["product_name"],
                    "quantity": args["quantity"],
                    "price": args["price"]
                })
                return build_response(item, "Item updated")
        return build_response(None, "Item not found", 404)

    def delete(self, item_id):
        global cart_items
        for item in cart_items:
            if item["id"] == item_id:
                cart_items = [i for i in cart_items if i["id"] != item_id]
                return build_response(None, "Item removed", 200)
        return build_response(None, "Item not found", 404)

class CartTotal(Resource):
    def get(self):
        total = sum(item["quantity"] * item["price"] for item in cart_items)
        return build_response({ "total_price": total }, "Cart total calculated")

# Routes
api.add_resource(Cart, "/cart")
api.add_resource(CartItem, "/cart/<int:item_id>")
api.add_resource(CartTotal, "/cart/total")

if __name__ == "__main__":
    app.run(debug=True)