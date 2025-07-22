from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class EmployeeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    position = StringField("Position", validators=[DataRequired()])
    department = StringField("Department", validators=[DataRequired()])
    salary = FloatField("Salary", validators=[DataRequired()])
    submit = SubmitField("Save")