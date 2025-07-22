from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class ExpenseForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    amount = FloatField("Amount", validators=[DataRequired()])
    category = SelectField("Category", choices=["Food", "Travel", "Utilities", "Entertainment", "Other"])
    date = DateField("Date", format="%Y-%m-%d")
    submit = SubmitField("Save")