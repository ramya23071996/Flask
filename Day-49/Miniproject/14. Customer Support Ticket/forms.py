from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SupportTicketForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    category = SelectField("Issue Category", choices=[
        ("billing", "Billing"),
        ("technical", "Technical"),
        ("account", "Account"),
        ("other", "Other")
    ], validators=[DataRequired()])
    description = TextAreaField("Issue Description", validators=[
        DataRequired(), Length(min=25, message="Please provide at least 25 characters.")
    ])
    submit = SubmitField("Submit Ticket")
