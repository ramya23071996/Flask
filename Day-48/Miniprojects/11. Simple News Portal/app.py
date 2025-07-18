from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/news")
def news():
    headlines = [
        {
            "title": "New AI Model Released",
            "datetime": datetime(2025, 7, 18, 9, 30),
            "category": "tech",
            "is_breaking": True
        },
        {
            "title": "Global Markets Rally",
            "datetime": datetime(2025, 7, 18, 11, 0),
            "category": "finance",
            "is_breaking": False
        },
        {
            "title": "Monsoon Hits Kerala",
            "datetime": datetime(2025, 7, 18, 6, 45),
            "category": "weather",
            "is_breaking": True
        }
    ]
    return render_template("news.html", headlines=headlines)

if __name__ == "__main__":
    app.run(debug=True)