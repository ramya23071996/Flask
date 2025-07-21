from flask import Flask, render_template, flash
from forms import SubscriptionForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    form = SubscriptionForm()

    if form.validate_on_submit():
        flash("Subscribed successfully!", "success")
        # Normally you’d save to a DB here
        return render_template('subscribe.html', form=form)

    return render_template('subscribe.html', form=form)
