from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    date = DateField("Appointment Date", validators=[DataRequired()])
    time = TimeField("Appointment Time", validators=[DataRequired()])
    purpose = TextAreaField("Purpose", validators=[DataRequired()])
    submit = SubmitField("Book Appointment")
