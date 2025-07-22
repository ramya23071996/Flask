from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

class StudentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    roll_no = StringField("Roll No", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    age = IntegerField("Age", validators=[DataRequired()])
    submit = SubmitField("Save")