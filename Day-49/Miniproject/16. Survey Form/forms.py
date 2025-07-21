from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class SurveyForm(FlaskForm):
    age = IntegerField("Age", validators=[
        DataRequired(), NumberRange(min=18, max=100, message="Age must be between 18 and 100")
    ])
    gender = RadioField("Gender", choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                        validators=[DataRequired()])
    favorite_product = SelectField("Favorite Product", choices=[
        ('', 'Select One'), ('Laptop', 'Laptop'), ('Phone', 'Phone'), ('Tablet', 'Tablet')
    ], validators=[DataRequired()])
    feedback = TextAreaField("Your Feedback", validators=[DataRequired()])
    submit = SubmitField("Submit Survey")
