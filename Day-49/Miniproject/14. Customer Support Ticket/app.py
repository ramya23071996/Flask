from flask import Flask, render_template, flash
from forms import SupportTicketForm
import random
import string

app = Flask(__name__)
app.secret_key = "ticketsecretkey"

def generate_ticket_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@app.route("/support", methods=["GET", "POST"])
def support():
    form = SupportTicketForm()
    if form.validate_on_submit():
        ticket_id = generate_ticket_id()
        flash(f"Support ticket created! Your Ticket ID is: {ticket_id}", "success")
    return render_template("support.html", form=form)
