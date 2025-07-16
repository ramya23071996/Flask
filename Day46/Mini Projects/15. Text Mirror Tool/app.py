from flask import Flask

app = Flask(__name__)

@app.route("/mirror/<text>")
def mirror_text(text):
    print(f"Accessed: /mirror/{text}")
    reversed_text = text[::-1]
    length = len(text)

    return f"""
    <html>
    <head>
        <title>Text Mirror Tool</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 30px; background: #f5f5f5; }}
            h2 {{ color: #333; }}
            table {{ border-collapse: collapse; margin-top: 20px; width: 60%; }}
            th, td {{ border: 1px solid #ccc; padding: 10px; text-align: left; }}
            th {{ background-color: #eaeaea; }}
            pre {{ background-color: #f0f0f0; padding: 15px; border-radius: 8px; }}
        </style>
    </head>
    <body>
        <h2>Text Mirror Result</h2>
        <pre>
Original: {text}
Reversed: {reversed_text}
Length:   {length}
        </pre>
        <table>
            <tr><th>Original</th><th>Reversed</th><th>Length</th></tr>
            <tr><td>{text}</td><td>{reversed_text}</td><td>{length}</td></tr>
        </table>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)