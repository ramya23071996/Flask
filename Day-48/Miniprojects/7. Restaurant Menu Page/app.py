from flask import Flask, render_template

app = Flask(__name__)

@app.route("/menu")
def menu():
    menu_data = {
        "Starters": [
            {"name": "Tomato Soup", "image": "soup.jpg", "available": True},
            {"name": "Garlic Bread", "image": "bread.jpg", "available": False}
        ],
        "Main Course": [
            {"name": "Pasta Alfredo", "image": "pasta.jpg", "available": True},
            {"name": "Grilled Chicken", "image": "chicken.jpg", "available": True}
        ],
        "Desserts": [
            {"name": "Chocolate Cake", "image": "cake.jpg", "available": False},
            {"name": "Ice Cream", "image": "icecream.jpg", "available": True}
        ]
    }
    return render_template("menu.html", menu=menu_data)

if __name__ == "__main__":
    app.run(debug=True)