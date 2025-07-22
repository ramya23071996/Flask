from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    phone = StringField("Phone", validators=[
        DataRequired(),
        Regexp(r'^[0-9\-+() ]+$', message="Invalid phone format")
    ])
    email = StringField("Email", validators=[DataRequired(), Email()])
    address = TextAreaField("Address", validators=[DataRequired()])
    submit = SubmitField("Save")