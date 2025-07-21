from flask import Flask, render_template, flash
from forms import ComplaintForm
import random

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route("/complaint", methods=["GET", "POST"])
def complaint():
    form = ComplaintForm()
    if form.validate_on_submit():
        complaint_id = random.randint(10000, 99999)
        flash(f"Complaint #{complaint_id} registered successfully!", "success")
    return render_template("complaint.html", form=form)
