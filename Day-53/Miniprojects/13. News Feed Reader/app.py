from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample headlines by category
news_data = {
    "Technology": [
        "AI models surpass human benchmarks",
        "New quantum computing breakthrough",
        "Cybersecurity tips for modern teams"
    ],
    "Sports": [
        "India clinches Test series",
        "Olympic qualifiers begin in Paris",
        "Football transfers heat up in Europe"
    ]
}

@app.route('/')
def index():
    default_category = 'Technology'
    return render_template('news.html', category=default_category)

@app.route('/api/news')
def get_news():
    category = request.args.get('category', 'Technology')
    headlines = news_data.get(category, [])
    return jsonify({"headlines": headlines})