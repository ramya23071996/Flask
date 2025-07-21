from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email

class BugReportForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[
        DataRequired(),
        Email(message="Enter a valid email address.")
    ])
    description = TextAreaField("Bug Description", validators=[DataRequired()])
    severity = RadioField("Severity", choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], validators=[DataRequired()])
    submit = SubmitField("Submit Bug Report")
