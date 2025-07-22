from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    date = DateField("Date", format="%Y-%m-%d", validators=[DataRequired()])
    time = TimeField("Time", format="%H:%M", validators=[DataRequired()])
    status = SelectField("Status", choices=["Pending", "Confirmed", "Canceled"])
    submit = SubmitField("Save")