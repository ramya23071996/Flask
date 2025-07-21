from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ComplaintForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    category = SelectField("Category", choices=[
        ("service", "Service Issue"),
        ("billing", "Billing Problem"),
        ("technical", "Technical Error"),
        ("other", "Other")
    ], validators=[DataRequired()])
    complaint = TextAreaField("Complaint", validators=[DataRequired(), Length(min=15)])
    submit = SubmitField("Submit Complaint")
