USERS = [{"id": i, "name": f"User{i}", "status": "active" if i%2==0 else "inactive"} for i in range(1, 21)]
PRODUCTS = [
    {"name": "Laptop", "price": 50000, "in_stock": True},
    {"name": "Mouse", "price": 1000, "in_stock": False},
    {"name": "Keyboard", "price": 1500, "in_stock": True}
]
MESSAGES = ["Keep coding!", "Flask FTW!", "Modular APIs rock!"]
APP_VERSION = "2.1.0"