from flask import Flask, request, jsonify, render_template
from task_data import feedback_examples

app = Flask(__name__)
feedback_list = feedback_examples.copy()  # seed from external file

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/feedback', methods=['POST'])
def collect_feedback():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')
    if name and message:
        feedback_list.append({'name': name, 'message': message})
        return jsonify({'status': 'success'}), 201
    return jsonify({'status': 'error', 'msg': 'Invalid input'}), 400

@app.route('/api/feedbacks')
def get_feedbacks():
    return jsonify({'feedbacks': feedback_list})