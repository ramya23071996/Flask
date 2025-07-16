from flask import Flask

app = Flask(__name__)

@app.route("/zodiac/<date>")
def get_zodiac(date):
    print(f"Accessed: /zodiac/{date}")
    try:
        year, month, day = map(int, date.split("-"))
        # Dummy logic: assign sign by month only
        signs = {
            1: "Capricorn", 2: "Aquarius", 3: "Pisces",
            4: "Aries", 5: "Taurus", 6: "Gemini",
            7: "Cancer", 8: "Leo", 9: "Virgo",
            10: "Libra", 11: "Scorpio", 12: "Sagittarius"
        }
        sign = signs.get(month, "Unknown")
        return f"""
        <html>
        <body style="font-family:Verdana; padding:30px;">
            <strong>Zodiac Sign:</strong> <i>{sign}</i>
            <hr>
            <p>Hello! Based on your birthdate of <strong>{date}</strong>, your zodiac sign is <i>{sign}</i>.</p>
        </body>
        </html>
        """
    except ValueError:
        return "<strong>Invalid date format. Please use YYYY-MM-DD.</strong>"

@app.route("/zodiac/help")
def help_page():
    print("Accessed: /zodiac/help")
    return """
    <html>
    <body style="font-family:Arial; padding:30px;">
        <strong>Help Guide</strong>
        <hr>
        <p>Use the format <i>YYYY-MM-DD</i> in the URL to get your Zodiac sign.</p>
        <p>Example: <strong>/zodiac/1990-07-15</strong></p>
        <p>This will return the Zodiac sign for someone born on July 15, 1990.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)