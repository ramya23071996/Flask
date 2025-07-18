from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        hobbies = request.form.get('hobbies')
        hobby_list = [h.strip() for h in hobbies.split(',')] if hobbies else []
        return render_template('bio.html', name=name, age=age, hobbies=hobby_list)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
