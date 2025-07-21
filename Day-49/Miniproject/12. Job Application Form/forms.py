from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, URL, NumberRange

class JobApplicationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    resume_url = StringField("Resume URL", validators=[DataRequired(), URL(message="Please enter a valid URL.")])
    experience = IntegerField("Years of Experience", validators=[DataRequired(), NumberRange(min=0, message="Experience must be 0 or more.")])
    submit = SubmitField("Apply")
