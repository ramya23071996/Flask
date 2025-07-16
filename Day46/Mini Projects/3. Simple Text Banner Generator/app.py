from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <b>Enter your banner text</b>
    <p>Try this link → <a href="/banner/Hello">/banner/Hello</a></p>
    <hr>
    """

@app.route("/banner/<text>")
def banner(text):
    return f"<h1>{text}</h1><hr>"

@app.route("/banner/<text>/<size>")
def banner_with_size(text, size):
    valid_sizes = [f"h{i}" for i in range(1, 7)]
    if size.lower() in valid_sizes:
        return f"<{size}>{text}</{size}><hr>"
    else:
        return "<p>Invalid size. Use h1 to h6 only.</p><hr>"
    
if __name__ == "__main__":
    app.run(debug=True)