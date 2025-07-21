from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

class ReviewForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email(message="Enter a valid email address.")])
    rating = IntegerField("Rating (1–5)", validators=[DataRequired(), NumberRange(min=1, max=5, message="Rating must be between 1 and 5.")])
    message = TextAreaField("Review", validators=[DataRequired()])
    submit = SubmitField("Submit Review")
