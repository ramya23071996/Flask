from flask import Flask

app = Flask(__name__)

@app.route("/preview/<site>")
def preview(site):
    print(f"Accessed: /preview/{site}")
    return f"""
    <html>
    <head>
        <title>Preview - {site}.com</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 40px; background-color: #fdfdfd; }}
            h1 {{ color: #2c3e50; }}
            p {{ font-size: 1.2em; color: #555; }}
        </style>
    </head>
    <body>
        <h1>{site.capitalize()} Preview</h1>
        <p>This is a simulated preview of <strong>{site}.com</strong>.</p>
        <p>Get a quick idea of what the site might be about before you visit!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    