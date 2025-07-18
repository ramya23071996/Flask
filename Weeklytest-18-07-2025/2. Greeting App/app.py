from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    lang = request.args.get('lang', 'en')
    return render_template('greet.html', name=name, lang=lang)

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)