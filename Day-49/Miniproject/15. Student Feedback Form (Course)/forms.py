from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Optional

class FeedbackForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    course = StringField("Course", validators=[DataRequired()])
    rating = IntegerField("Rating (1–10)", validators=[
        DataRequired(), NumberRange(min=1, max=10, message="Rating must be between 1 and 10")
    ])
    suggestion = TextAreaField("Suggestion (optional)", validators=[Optional()])
    submit = SubmitField("Submit Feedback")
