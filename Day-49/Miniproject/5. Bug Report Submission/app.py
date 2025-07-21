from flask import Flask, render_template, flash
from forms import BugReportForm

app = Flask(__name__)
app.secret_key = "bugreportsecret"

@app.route('/bug-report', methods=['GET', 'POST'])
def bug_report():
    form = BugReportForm()

    if form.validate_on_submit():
        severity = form.severity.data
        if severity == 'low':
            flash("Thanks for the report! We'll review it soon. (Low Severity)", "info")
        elif severity == 'medium':
            flash("Thanks! This bug has been flagged for review. (Medium Severity)", "warning")
        elif severity == 'high':
            flash("Critical alert! Our team has been notified. (High Severity)", "danger")
        return render_template("bug_report.html", form=form)

    return render_template("bug_report.html", form=form)
