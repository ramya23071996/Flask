from flask import Flask, render_template, redirect, url_for, request
from forms import UserInfoForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserInfoForm()

    # Set default values
    if request.method == 'GET':
        form.name.data = 'John Doe'
        form.country.data = 'IN'
        form.lucky_number.data = 7
        form.comment.data = 'Default comment'

    if form.validate_on_submit():
        print("Name:", form.name.data)
        print("Email:", form.email.data)
        print("Message:", form.message.data)
        print("Gender:", form.gender.data)
        print("Country:", form.country.data)
        print("Accepted Terms:", form.accept_terms.data)
        print("Password:", form.password.data)
        print("Comment:", form.comment.data)
        print("Birth Date:", form.birth_date.data)
        print("Lucky Number:", form.lucky_number.data)

        return render_template("success.html", form=form)

    return render_template("form.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
