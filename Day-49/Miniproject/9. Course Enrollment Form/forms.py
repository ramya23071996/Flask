from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

class EnrollmentForm(FlaskForm):
    student_name = StringField("Student Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email(message="Enter a valid email address.")])
    course = SelectField("Course", choices=[
        ('python', 'Python Programming'),
        ('web', 'Web Development'),
        ('data', 'Data Science')
    ], validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=18, max=60, message="Age must be between 18 and 60.")])
    submit = SubmitField("Enroll")
