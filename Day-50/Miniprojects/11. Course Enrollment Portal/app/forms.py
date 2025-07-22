from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class EnrollmentForm(FlaskForm):
    student_id = SelectField("Student", coerce=int, validators=[DataRequired()])
    course_id = SelectField("Course", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Enroll")