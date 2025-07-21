from flask import Flask, render_template, flash
from forms import BookingForm

app = Flask(__name__)
app.secret_key = "securebookingkey"

@app.route("/book", methods=["GET", "POST"])
def book():
    form = BookingForm()
    if form.validate_on_submit():
        name = form.full_name.data
        nights = form.nights.data
        room = form.room_type.data
        flash(f"Booking for {name} confirmed: {nights} nights in {room.title()}!", "success")
    return render_template("booking.html", form=form)
