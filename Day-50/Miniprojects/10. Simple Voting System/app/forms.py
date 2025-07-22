from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class VoteForm(FlaskForm):
    voter_name = StringField("Your Name", validators=[DataRequired()])
    candidate_id = SelectField("Choose Candidate", coerce=int)
    submit = SubmitField("Cast Vote")