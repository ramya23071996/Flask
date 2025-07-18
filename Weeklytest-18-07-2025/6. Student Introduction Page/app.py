from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/student/<name>")
def student_intro(name):
    age = request.args.get("age")
    course = request.args.get("course")

    return render_template("student.html", name=name, age=age, course=course)

if __name__ == "__main__":
    app.run(debug=True)