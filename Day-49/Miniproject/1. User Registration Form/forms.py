from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    full_name = StringField("Full Name", validators=[
        DataRequired(message="Name is required."),
        Length(min=3, message="Name must be at least 3 characters.")
    ])
    email = StringField("Email", validators=[
        DataRequired(message="Email is required."),
        Email(message="Enter a valid email.")
    ])
    password = PasswordField("Password", validators=[
        DataRequired(message="Password is required."),
        Length(min=6, message="Password must be at least 6 characters.")
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(message="Please confirm your password."),
        EqualTo("password", message="Passwords must match.")
    ])
    submit = SubmitField("Register")
