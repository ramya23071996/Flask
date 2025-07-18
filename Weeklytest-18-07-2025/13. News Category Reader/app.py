from flask import Flask, render_template

app = Flask(__name__)

# Simulated news content by category
news_data = {
    "technology": [
        "AI beats humans in medical diagnostics",
        "Quantum computing breakthrough at IBM",
        "Google launches new Android version"
    ],
    "sports": [
        "India wins T20 World Cup!",
        "Olympics 2024 preview: What to expect",
        "Messi scores a hat trick in finals"
    ],
    "politics": [
        "Elections 2025: Major parties gear up",
        "New tax bill passed in parliament",
        "Global leaders meet for climate summit"
    ]
}

@app.route('/news/<category>')
def news(category):
    articles = news_data.get(category.lower())
    if not articles:
        return f"<h2>No news available for category: {category}</h2>"
    return render_template("news.html", category=category.title(), articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
