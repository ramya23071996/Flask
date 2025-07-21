from flask import Flask, render_template
from forms import ValidationForm

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ValidationForm()
    error_count = 0

    if form.validate_on_submit():
        return f"<h3>Form submitted successfully!</h3>"

    if form.errors:
        error_count = sum(len(errs) for errs in form.errors.values())

    return render_template('form.html', form=form, error_count=error_count)

if __name__ == '__main__':
    app.run(debug=True)
