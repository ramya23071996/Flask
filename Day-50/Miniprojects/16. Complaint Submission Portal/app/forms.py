from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ComplaintForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    message = TextAreaField("Complaint Message", validators=[DataRequired()])
    resolved = BooleanField("Resolved?")
    submit = SubmitField("Save")