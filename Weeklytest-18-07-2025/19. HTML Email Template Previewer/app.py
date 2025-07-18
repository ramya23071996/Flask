from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        # Simulated data for placeholders
        context = {
            'username': 'John Doe',
            'product': 'Flask Pro Course',
            'discount': '20%'
        }
        return render_template('preview.html', title=title, body=body, **context)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
