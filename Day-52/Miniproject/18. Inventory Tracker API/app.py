from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

inventory = []
item_id_counter = 1
LOW_STOCK_THRESHOLD = 5  # warning threshold

# Request parser
parser = reqparse.RequestParser()
parser.add_argument("item_name", required=True, help="Item name is required")
parser.add_argument("quantity", type=int, required=True, help="Quantity must be a positive integer")
parser.add_argument("category", required=True, help="Category is required")

# Response formatter
def build_response(data=None, message="", status=200):
    return { "message": message, "data": data }, status

# Resources
class InventoryList(Resource):
    def get(self):
        return build_response(inventory, "Inventory items retrieved")

    def post(self):
        global item_id_counter
        args = parser.parse_args()

        if args["quantity"] < 0:
            return build_response(None, "Quantity must be non-negative", 400)

        item = {
            "id": item_id_counter,
            "item_name": args["item_name"],
            "quantity": args["quantity"],
            "category": args["category"]
        }
        inventory.append(item)
        item_id_counter += 1
        return build_response(item, "Item added", 201)

class InventoryItem(Resource):
    def put(self, item_id):
        args = parser.parse_args()

        if args["quantity"] < 0:
            return build_response(None, "Quantity must be non-negative", 400)

        for item in inventory:
            if item["id"] == item_id:
                item.update({
                    "item_name": args["item_name"],
                    "quantity": args["quantity"],
                    "category": args["category"]
                })
                if args["quantity"] < LOW_STOCK_THRESHOLD:
                    return build_response(item, "Warning: Low stock level", 200)
                return build_response(item, "Item updated")
        return build_response(None, "Item not found", 404)

    def delete(self, item_id):
        global inventory
        for item in inventory:
            if item["id"] == item_id:
                inventory = [i for i in inventory if i["id"] != item_id]
                return build_response(None, "Item deleted", 200)
        return build_response(None, "Item not found", 404)

# Routing
api.add_resource(InventoryList, "/inventory")
api.add_resource(InventoryItem, "/inventory/<int:item_id>")

if __name__ == "__main__":
    app.run(debug=True)