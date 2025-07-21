from flask import Flask, render_template, flash
from forms import RSVPForm

app = Flask(__name__)
app.secret_key = "rsvpeventsecret"

@app.route("/rsvp", methods=["GET", "POST"])
def rsvp():
    form = RSVPForm()
    
    if form.validate_on_submit():
        if form.will_attend.data:
            flash(f"Thanks {form.name.data}! We look forward to seeing you.", "success")
        else:
            flash("Sorry to miss you!", "warning")
        return render_template("rsvp.html", form=form)

    return render_template("rsvp.html", form=form)
