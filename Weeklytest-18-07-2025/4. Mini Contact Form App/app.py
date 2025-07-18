from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return redirect(url_for('thank_you', name=name, email=email, message=message))
    return render_template('contact.html')

@app.route('/thankyou/<name>')
def thank_you(name):
    email = request.args.get('email')
    message = request.args.get('message')
    return render_template('thankyou.html', name=name, email=email, message=message)

if __name__ == '__main__':
    app.run(debug=True)