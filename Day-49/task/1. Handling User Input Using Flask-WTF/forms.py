from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField, BooleanField, PasswordField, TextAreaField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

class UserInfoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    
    gender = RadioField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    country = SelectField('Country', choices=[('IN', 'India'), ('US', 'USA'), ('UK', 'UK')], validators=[DataRequired()])
    accept_terms = BooleanField('I accept the Terms & Conditions', validators=[DataRequired()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    
    comment = TextAreaField('Comment')
    birth_date = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired()])
    lucky_number = IntegerField('Lucky Number', validators=[DataRequired()])
    
    submit = SubmitField('Submit')
