from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory application store (for demo purposes)
applications = []

# 1. /apply – form to submit job application
@app.route('/apply', methods=['GET'])
def apply():
    return '''
    <h2>Job Application Form</h2>
    <form method="POST" action="/submit-application">
        Name: <input type="text" name="name"><br>
        Email: <input type="email" name="email"><br>
        Position: 
        <select name="position">
            <option value="Python">Python Developer</option>
            <option value="Frontend">Frontend Developer</option>
            <option value="Data">Data Analyst</option>
        </select><br>
        <input type="submit" value="Apply">
    </form>
    '''

# 2. /submit-application – handle POST and redirect
@app.route('/submit-application', methods=['POST'])
def submit_application():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    position = request.form.get('position', '').strip()

    # Store application
    applications.append({
        'name': name,
        'email': email,
        'position': position
    })

    # Redirect to status page with name as query param
    return redirect(url_for('application_status', name=name))

# 3. /application-status – confirmation page
@app.route('/application-status')
def application_status():
    name = request.args.get('name', 'Applicant')
    return f"<h3>Thank you, {escape(name)}! Your application has been submitted.</h3>"

# 4. /applications?position=Python – filter by position
@app.route('/applications')
def view_applications():
    position = request.args.get('position', '').strip().lower()
    filtered = [a for a in applications if a['position'].lower() == position] if position else applications

    if not filtered:
        return f"<p>No applications found for position: {escape(position)}</p>"

    items = "".join([
        f"<li><strong>{escape(a['name'])}</strong> ({escape(a['email'])}) – {escape(a['position'])}</li>"
        for a in filtered
    ])
    return f"<h3>Applications</h3><ul>{items}</ul>"

# 5. /applicant/<name> – show individual applicant
@app.route('/applicant/<name>')
def applicant(name):
    matches = [a for a in applications if a['name'].lower() == name.lower()]
    if not matches:
        return f"<p>No application found for: {escape(name)}</p>"

    a = matches[0]
    return f"""
    <h3>Applicant: {escape(a['name'])}</h3>
    <p>Email: {escape(a['email'])}</p>
    <p>Position: {escape(a['position'])}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)