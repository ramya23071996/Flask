from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        choice = request.form.get('vote')
        return render_template('result.html', choice=choice)
    return render_template('poll.html')

if __name__ == '__main__':
    app.run(debug=True)
