from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/greet')
def greet():
    hour_str = request.args.get('hour')
    try:
        hour = int(hour_str)
        if hour < 0 or hour > 23:
            raise ValueError
    except (TypeError, ValueError):
        hour = None
    return render_template('greet.html', hour=hour)

if __name__ == '__main__':
    app.run(debug=True)
