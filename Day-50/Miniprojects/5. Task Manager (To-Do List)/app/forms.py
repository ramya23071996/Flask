from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField("Task", validators=[DataRequired()])
    due_date = DateField("Due Date (YYYY-MM-DD)", format="%Y-%m-%d")
    is_done = BooleanField("Completed")
    submit = SubmitField("Save")