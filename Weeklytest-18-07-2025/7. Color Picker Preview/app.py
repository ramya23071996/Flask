from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    color = "#ffffff"  # default color: white
    if request.method == 'POST':
        color_input = request.form.get('color')
        if color_input:
            color = color_input
    return render_template('index.html', color=color)

if __name__ == '__main__':
    app.run(debug=True)
