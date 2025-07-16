from flask import Flask, request, redirect, url_for, escape

app = Flask(__name__)

# In-memory bug report store
bug_reports = []
bug_id_counter = 1  # Simple ID generator

# 1. /report – form to submit a bug
@app.route('/report', methods=['GET'])
def report_form():
    return '''
    <h2>Submit a Bug Report</h2>
    <form method="POST" action="/submit-report">
        Title: <input type="text" name="title"><br>
        Description: <textarea name="description"></textarea><br>
        Priority:
        <select name="priority">
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
        </select><br>
        <input type="submit" value="Submit Bug">
    </form>
    '''

# 2. /submit-report – handle POST and redirect
@app.route('/submit-report', methods=['POST'])
def submit_report():
    global bug_id_counter
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    priority = request.form.get('priority', 'low').strip().lower()

    # Save bug report
    bug_reports.append({
        'id': bug_id_counter,
        'title': title,
        'description': description,
        'priority': priority
    })
    bug_id_counter += 1

    return redirect(url_for('report_confirm'))

# 3. /report-confirm – confirmation page
@app.route('/report-confirm')
def report_confirm():
    return "<h3>✅ Bug report submitted successfully!</h3>"

# 4. /bugs?priority=high – filter by priority
@app.route('/bugs')
def view_bugs():
    priority = request.args.get('priority', '').strip().lower()
    filtered = [b for b in bug_reports if b['priority'] == priority] if priority else bug_reports

    if not filtered:
        return f"<p>No bugs found with priority: {escape(priority)}</p>"

    items = "".join([
        f"<li><a href='/bug/{b['id']}'>#{b['id']} - {escape(b['title'])}</a> ({escape(b['priority'].capitalize())})</li>"
        for b in filtered
    ])
    return f"<h3>Bug Reports</h3><ul>{items}</ul>"

# 5. /bug/<id> – dynamic bug detail view
@app.route('/bug/<int:id>')
def bug_detail(id):
    match = next((b for b in bug_reports if b['id'] == id), None)
    if match:
        return f"""
        <h3>Bug #{match['id']}</h3>
        <p><strong>Title:</strong> {escape(match['title'])}</p>
        <p><strong>Description:</strong> {escape(match['description'])}</p>
        <p><strong>Priority:</strong> {escape(match['priority'].capitalize())}</p>
        """
    return f"<p>Bug with ID #{id} not found.</p>"

if __name__ == '__main__':
    app.run(debug=True)