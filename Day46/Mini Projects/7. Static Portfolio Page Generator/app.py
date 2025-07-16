from flask import Flask

app = Flask(__name__)

@app.route("/portfolio/<name>")
def portfolio(name):
    return f"""
    <h2>Welcome to {name}'s Portfolio</h2>
    <p>Full Stack Developer & UI/UX Enthusiast</p>
    <hr>
    <p>Explore my <a href='/portfolio/{name}/skills'>skills</a> and <a href='/portfolio/{name}/projects'>projects</a>.</p>
    """

@app.route("/portfolio/<name>/skills")
def skills(name):
    skills_list = [
        "HTML, CSS, JavaScript",
        "Python scripting and automation",
        "SQL database design",
        "Responsive UI/UX implementation",
        "Modular CLI tools"
    ]
    items = "".join(f"<li>{skill}</li>" for skill in skills_list)
    return f"""
    <h2>{name}'s Skills</h2>
    <ul>{items}</ul>
    <hr>
    <a href='/portfolio/{name}'>← Back to Profile</a>
    """

@app.route("/portfolio/<name>/projects")
def projects(name):
    projects = [
        {"title": "VTS Exam Portal", "tech": "Flask, HTML/CSS, Responsive UI"},
        {"title": "Disk Usage CLI Tool", "tech": "Python, Argparse"},
        {"title": "Digital Visiting Card", "tech": "Flask, Jinja2 Routing"},
        {"title": "Business Hours Page", "tech": "Flask, Datetime"}
    ]
    rows = "".join(f"<tr><td>{p['title']}</td><td>{p['tech']}</td></tr>" for p in projects)
    return f"""
    <h2>{name}'s Projects</h2>
    <table border='1' cellpadding='8'>
        <tr><th>Project</th><th>Technologies</th></tr>
        {rows}
    </table>
    <hr>
    <a href='/portfolio/{name}'>← Back to Profile</a>
    """
    
if __name__ == "__main__":
    app.run(debug=True)