from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class PasswordResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    new_password = PasswordField("New Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(), EqualTo("new_password", message="Passwords must match")
    ])
    submit = SubmitField("Reset Password")
