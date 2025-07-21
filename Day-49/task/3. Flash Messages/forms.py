from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

class FlashForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1)])
    password = PasswordField('Password', validators=[DataRequired()])
    accept_terms = BooleanField('I accept terms')
    submit = SubmitField('Submit')
