from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/age/<name>/<int:year>")
def check_age(name, year):
    current_year = datetime.now().year
    print(f"Accessed: /age/{name}/{year}")
    
    if year >= current_year:
        message = f"Hi {name}, year must be less than {current_year}!"
    else:
        age = current_year - year
        message = f"Hi {name}, you are {age} years old."

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Age Checker</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #fefefe; text-align: center; padding: 40px; }}
            .msg {{ background-color: #d1e7dd; color: #0f5132; border: 1px solid #badbcc; 
                   padding: 20px; font-size: 1.6em; max-width: 600px; margin: auto; border-radius: 10px; }}
        </style>
    </head>
    <body>
        <div class="msg">{message}</div>
    </body>
    </html>
    """
    
if __name__ == "__main__":
    app.run(debug=True, port=5050, host="0.0.0.0")  # Custom IP and port