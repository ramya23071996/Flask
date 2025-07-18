from flask import Flask, render_template

app = Flask(__name__)

@app.route("/result")
def result():
    student = {
        "name": "Ramya",
        "grade": "A",
        "subjects": {
            "Math": 95,
            "Science": 88,
            "English": 92,
            "History": 85
        }
    }
    return render_template("result.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)