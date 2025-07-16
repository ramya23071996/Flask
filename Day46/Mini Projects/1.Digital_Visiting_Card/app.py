from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Ramya</h1>
    <p>Full Stack Developer & UI/UX Enthusiast</p>
    <p>Contact: ramya@example.com</p>
    """

@app.route("/about")
def about():
    return "I build polished, responsive web apps and automation tools using Python, JavaScript, SQL, and more."

@app.route("/skills/<name>")
def skills(name):
    skill_sets = {
        "ramya": [
            "HTML, CSS, JavaScript",
            "Python scripting",
            "SQL database design",
            "Responsive UI/UX",
            "Automation & CLI tools"
        ],
        "alex": ["React", "Node.js", "Docker", "AWS"]
    }
    return "<ul>" + "".join(f"<li>{skill}</li>" for skill in skill_sets.get(name.lower(), ["No skills found"])) + "</ul>"

if __name__ == "__main__":
    app.run(debug=True)