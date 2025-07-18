from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        experience = request.form.get('experience')
        return render_template('resume.html', name=name, email=email, experience=experience)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
