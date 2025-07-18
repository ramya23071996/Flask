from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
feedback_list = []

@app.route('/')
def home():
    return render_template('feedback.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    feedback_list.append({'name': name, 'message': message})
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thankyou.html')

@app.route('/view-feedback')
def view_feedback():
    return render_template('view_feedback.html', feedback=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)