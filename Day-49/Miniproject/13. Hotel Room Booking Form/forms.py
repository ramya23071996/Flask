from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

class BookingForm(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    room_type = SelectField("Room Type", choices=[
        ("single", "Single Room"),
        ("double", "Double Room"),
        ("suite", "Suite")
    ], validators=[DataRequired()])
    nights = IntegerField("Number of Nights", validators=[
        DataRequired(), NumberRange(min=1, message="Stay must be at least 1 night.")
    ])
    submit = SubmitField("Book Now")
