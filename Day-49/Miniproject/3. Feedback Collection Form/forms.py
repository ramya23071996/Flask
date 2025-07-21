from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Email

class FeedbackForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email (optional)", validators=[Optional(), Email(message="Enter a valid email.")])
    message = TextAreaField("Message", validators=[
        DataRequired(message="Message is required."),
        Length(min=10, message="Message must be at least 10 characters.")
    ])
    submit = SubmitField("Send Feedback")
