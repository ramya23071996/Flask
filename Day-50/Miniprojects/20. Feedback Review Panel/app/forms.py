from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class FeedbackForm(FlaskForm):
    user_name = StringField("Your Name", validators=[DataRequired()])
    rating = IntegerField("Rating (1–5)", validators=[DataRequired(), NumberRange(min=1, max=5)])
    comment = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")