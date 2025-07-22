from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    published_year = IntegerField("Published Year", validators=[DataRequired()])
    submit = SubmitField("Save")