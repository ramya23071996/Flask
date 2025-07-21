from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

class GymSignupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=16, message="You must be at least 16 years old")])
    email = StringField("Email", validators=[DataRequired(), Email()])
    plan = SelectField("Membership Plan", choices=[
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ], validators=[DataRequired()])
    terms = BooleanField("I accept the terms and conditions", validators=[DataRequired(message="You must accept the terms")])
    submit = SubmitField("Join Now")
