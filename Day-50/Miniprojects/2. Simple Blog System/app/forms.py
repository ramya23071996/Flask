from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    submit = SubmitField("Save")