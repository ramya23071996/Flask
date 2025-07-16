from flask import Flask

app = Flask(__name__)

@app.route("/greet/<int:hour>")
def greet_by_hour(hour):
    print(f"Accessed: /greet/{hour}")
    if hour < 0 or hour > 23:
        greeting = "Invalid hour! Please enter a value between 0 and 23."
    elif hour < 12:
        greeting = "Good Morning 🌅"
    elif hour < 18:
        greeting = "Good Afternoon ☀️"
    else:
        greeting = "Good Night 🌙"

    return f"""
    <html>
    <head>
        <title>Greeter</title>
        <style>
            body {{ font-family: Helvetica, sans-serif; padding: 40px; background-color: #fdfdfd; }}
            h2 {{ color: #4a4a4a; }}
        </style>
    </head>
    <body>
        <h2>{greeting}</h2>
        <p>You entered hour: <strong>{hour}</strong></p>
    </body>
    </html>
    """

@app.route("/greet/info")
def greet_info():
    print("Accessed: /greet/info")
    return """
    <html>
    <head>
        <title>Greeter Info</title>
        <style>
            body { font-family: Verdana, sans-serif; padding: 40px; background-color: #f6f6f6; }
            ul { font-size: 1.1em; color: #333; }
        </style>
    </head>
    <body>
        <h2>Valid Hour Format</h2>
        <ul>
            <li>Use a number between <strong>0</strong> and <strong>23</strong>.</li>
            <li>Example: <i>/greet/8</i> returns “Good Morning”.</li>
            <li>Example: <i>/greet/15</i> returns “Good Afternoon”.</li>
        </ul>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)