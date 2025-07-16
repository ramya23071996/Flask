from flask import Flask

app = Flask(__name__)

@app.route("/wordcount/<text>")
def count_words(text):
    print(f"Accessed: /wordcount/{text}")
    word_count = len(text.split())
    return f"""
    <html>
    <head>
        <title>Word Counter</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 30px; background-color: #f4f4f4; }}
            h2 {{ color: #333; }}
            p {{ font-size: 1.2em; color: #555; }}
        </style>
    </head>
    <body>
        <h2>Word Count Result</h2>
        <p>The input text contains <strong>{word_count}</strong> word{'s' if word_count != 1 else ''}.</p>
    </body>
    </html>
    """

@app.route("/wordcount/help")
def help_page():
    print("Accessed: /wordcount/help")
    return """
    <html>
    <head>
        <title>Word Counter Help</title>
        <style>
            body { font-family: Verdana, sans-serif; padding: 30px; background-color: #fafafa; }
            h2 { color: #0066cc; }
            p { font-size: 1.1em; color: #333; }
        </style>
    </head>
    <body>
        <h2>How to Use the Word Counter</h2>
        <p>Use the route <strong>/wordcount/&lt;text&gt;</strong> to count words in your input.</p>
        <p>Example: <i>/wordcount/The quick brown fox</i> will return 4.</p>
    </body>
    </html>
    """
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)