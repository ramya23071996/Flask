from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample projects
projects = [
    {"id": 1, "title": "Portfolio Website", "description": "A personal portfolio built using Flask.", "tag": "web"},
    {"id": 2, "title": "Machine Learning Model", "description": "A predictive model using scikit-learn.", "tag": "ml"},
    {"id": 3, "title": "To-Do App", "description": "A task manager built with Flask.", "tag": "web"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def project_list():
    tag = request.args.get('tag')
    filtered_projects = [p for p in projects if p["tag"] == tag] if tag else projects
    return render_template('projects.html', projects=filtered_projects, tag=tag)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    return render_template('project_detail.html', project=project)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        # Normally save or send email here
        return redirect(url_for('contact_success'))
    return render_template('contact.html')

@app.route('/contact/success')
def contact_success():
    return "<h2>Thank you! Your message was sent successfully.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
