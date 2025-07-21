from flask import Flask, render_template, flash
from forms import FeedbackForm

app = Flask(__name__)
app.secret_key = 'feedbacksecret'

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()

    if form.validate_on_submit():
        flash("Thank you for your feedback!", "success")
        return render_template('feedback.html', form=form)

    return render_template('feedback.html', form=form)
