from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class BugForm(FlaskForm):
    title = StringField('Bug Title', validators=[DataRequired()])
    description = TextAreaField('Bug Description', validators=[DataRequired()])
    submit = SubmitField('Submit Bug')