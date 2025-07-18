from flask import Flask, render_template

app = Flask(__name__)

# Sample data
name = "Ramya"
skills = ["Python", "HTML", "CSS", "JavaScript", "Flask", "SQL"]
projects = [
    {"title": "Exam Portal", "description": "Online test system with results"},
    {"title": "Dashboard", "description": "Responsive admin dashboard"},
    {"title": "CLI File Search", "description": "Terminal-based file finder"},
]
available_for_hire = True

@app.route("/")
def home():
    return render_template("home.html", name=name, available=available_for_hire)

@app.route("/about")
def about():
    return render_template("about.html", name=name, skills=skills)

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)