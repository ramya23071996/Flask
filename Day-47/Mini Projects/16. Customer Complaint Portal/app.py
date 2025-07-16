from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory complaint log
complaints = []

# 1. /complaint – form to submit a complaint
@app.route('/complaint', methods=['GET'])
def complaint_form():
    return '''
    <h2>Submit a Complaint</h2>
    <form method="POST" action="/complaint-submit">
        Name: <input type="text" name="name"><br>
        Issue: <textarea name="issue"></textarea><br>
        Urgency:
        <select name="urgency">
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
        </select><br>
        <input type="submit" value="Submit Complaint">
    </form>
    '''

# 2. /complaint-submit – handle POST and redirect
@app.route('/complaint-submit', methods=['POST'])
def complaint_submit():
    name = request.form.get('name', 'Anonymous').strip()
    issue = request.form.get('issue', '').strip()
    urgency = request.form.get('urgency', 'low').strip().lower()

    # Store complaint
    complaints.append({
        'name': name,
        'issue': issue,
        'urgency': urgency
    })

    # Redirect to complaint status page
    return redirect(url_for('complaint_status', name=name))

# 3. /complaint-status/<name> – personalized status view
@app.route('/complaint-status/<name>')
def complaint_status(name):
    match = next((c for c in complaints if c['name'].lower() == name.lower()), None)
    if match:
        return f"""
        <h3>Complaint Status for {escape(match['name'])}</h3>
        <p><strong>Issue:</strong> {escape(match['issue'])}</p>
        <p><strong>Urgency:</strong> {escape(match['urgency'].capitalize())}</p>
        <p>We are reviewing your complaint. Thank you for your patience.</p>
        """
    return f"<p>No complaint found for {escape(name)}</p>"

# 4. /complaints?urgency=high – filter complaints by urgency
@app.route('/complaints')
def complaints_by_urgency():
    urgency = request.args.get('urgency', '').strip().lower()
    filtered = [c for c in complaints if c['urgency'] == urgency] if urgency else complaints

    if not filtered:
        return f"<p>No complaints found with urgency: {escape(urgency)}</p>"

    items = "".join([
        f"<li>{escape(c['name'])} – Issue: {escape(c['issue'])} (Urgency: {escape(c['urgency'].capitalize())})</li>"
        for c in filtered
    ])
    return f"<h3>Complaints</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)