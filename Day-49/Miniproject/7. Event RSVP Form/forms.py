from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class RSVPForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email(message="Enter a valid email address.")])
    will_attend = BooleanField("I will attend")
    submit = SubmitField("RSVP")
