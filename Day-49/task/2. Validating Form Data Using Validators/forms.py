from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import (
    DataRequired, Email, Length, EqualTo, NumberRange, Regexp, Optional, ValidationError
)

def block_test_email(form, field):
    if field.data.endswith('@test.com'):
        raise ValidationError('Email domain test.com is not allowed.')

class ValidationForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message='Name is required.'),
        Length(min=3, message='Name must be at least 3 characters.'),
        Regexp(r'^[A-Za-z]+$', message='Only alphabets are allowed.')
    ])
    
    username = StringField('Username', validators=[
        DataRequired(message='Username is required.'),
        Length(min=6, message='Username must be longer than 5 characters.')
    ])

    email = StringField('Email', validators=[
        DataRequired(message='Email is required.'),
        Email(message='Enter a valid email address.'),
        block_test_email
    ])

    age = IntegerField('Age', validators=[
        DataRequired(message='Age is required.'),
        NumberRange(min=18, max=60, message='Age must be between 18 and 60.')
    ])

    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required.')
    ])
    
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(message='Confirmation required.'),
        EqualTo('password', message='Passwords must match.')
    ])
    
    optional_nickname = StringField('Nickname', validators=[Optional()])
    
    submit = SubmitField('Register')
