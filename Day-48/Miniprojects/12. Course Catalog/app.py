from flask import Flask, render_template

app = Flask(__name__)

@app.route("/courses")
def courses():
    course_list = [
        {"title": "Intro to Python", "instructor": "Ramya", "duration": "6 weeks", "level": "beginner"},
        {"title": "Advanced Flask", "instructor": "Ramya", "duration": "4 weeks", "level": "advanced"},
        {"title": "UI/UX Fundamentals", "instructor": "Ramya", "duration": "5 weeks", "level": "intermediate"}
    ]
    return render_template("courses.html", courses=course_list)

if __name__ == "__main__":
    app.run(debug=True)