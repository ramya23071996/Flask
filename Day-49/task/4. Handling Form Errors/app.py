from flask import Flask, render_template, request
from forms import ErrorForm

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods=["GET", "POST"])
def index():
    form = ErrorForm()

    if form.validate_on_submit():
        # Successful submission
        return "<h3>Form submitted successfully!</h3>"

    elif request.method == "POST":
        # Form was submitted but invalid
        print("⚠️ Form Errors:")
        for field, errors in form.errors.items():
            for error in errors:
                print(f"{field}: {error}")

    return render_template("form.html", form=form)
