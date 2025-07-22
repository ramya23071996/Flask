from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Email

class SubscriberForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    plan = SelectField("Plan", choices=["Free", "Standard", "Premium"], validators=[DataRequired()])
    subscribed_on = DateTimeField("Subscription Date", format="%Y-%m-%d %H:%M", validators=[DataRequired()])
    submit = SubmitField("Save")