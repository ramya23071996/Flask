from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# Sample course catalog
course_catalog = [
    {'code': 'CS101', 'name': 'Intro to Computer Science', 'dept': 'CS'},
    {'code': 'CS201', 'name': 'Data Structures', 'dept': 'CS'},
    {'code': 'MATH101', 'name': 'Calculus I', 'dept': 'Math'},
    {'code': 'PHY101', 'name': 'Physics I', 'dept': 'Physics'},
    {'code': 'CS301', 'name': 'Algorithms', 'dept': 'CS'},
]

# In-memory registration store
registrations = []

# 1. /courses – show course list, filter by dept
@app.route('/courses')
def courses():
    dept = request.args.get('dept', '').strip().upper()
    filtered = [c for c in course_catalog if c['dept'] == dept] if dept else course_catalog

    if not filtered:
        return f"<p>No courses found for department: {escape(dept)}</p>"

    items = "".join([
        f"<li>{escape(c['code'])}: {escape(c['name'])} ({escape(c['dept'])})</li>"
        for c in filtered
    ])
    return f"<h3>Course List</h3><ul>{items}</ul>"

# 2. /register – show POST form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        course_code = request.form.get('course_code', '').strip().upper()

        # Store registration
        registrations.append({
            'name': name,
            'course_code': course_code
        })

        # Redirect to confirmation page
        return redirect(url_for('confirm_registration', name=name))

    return '''
    <h2>Course Registration</h2>
    <form method="POST">
        Student Name: <input type="text" name="name"><br>
        Course Code: <input type="text" name="course_code"><br>
        <input type="submit" value="Register">
    </form>
    '''

# 3. /confirm-registration/<name> – personalized confirmation
@app.route('/confirm-registration/<name>')
def confirm_registration(name):
    match = next((r for r in registrations if r['name'].lower() == name.lower()), None)
    if match:
        return f"""
        <h3>Registration Confirmed</h3>
        <p>Student: {escape(match['name'])}</p>
        <p>Course Code: {escape(match['course_code'])}</p>
        """
    return f"<p>No registration found for {escape(name)}</p>"

if __name__ == '__main__':
    app.run(debug=True)