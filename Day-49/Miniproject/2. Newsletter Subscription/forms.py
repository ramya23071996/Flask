from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class SubscriptionForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[
        DataRequired(message="Email is required."),
        Email(message="Enter a valid email address.")
    ])
    frequency = SelectField("Frequency", choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ], validators=[DataRequired()])
    
    submit = SubmitField("Subscribe")
