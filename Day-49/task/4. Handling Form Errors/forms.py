from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class ErrorForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3)])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=18, max=99)])
    submit = SubmitField("Submit")
