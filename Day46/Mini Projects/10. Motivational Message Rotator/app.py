from flask import Flask, render_template_string
import random

app = Flask(__name__)

messages = [
    "Believe in yourself and all that you are.",
    "Success is the sum of small efforts repeated day in and day out.",
    "Don't watch the clock; do what it does. Keep going.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Push yourself, because no one else is going to do it for you."
]

css_style = """
<style>
    body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 40px; text-align: center; }
    .quote { background: #ffffff; border-left: 10px solid #4CAF50; padding: 20px; font-size: 1.5em; color: #333; max-width: 600px; margin: auto; box-shadow: 2px 2px 15px rgba(0,0,0,0.1); }
</style>
"""

@app.route("/message")
def random_message():
    msg = random.choice(messages)
    print(f"Accessed: /message - Served random quote")
    return render_template_string(css_style + f"<div class='quote'>{msg}</div>")

@app.route("/message/<int:index>")
def message_by_index(index):
    if 0 <= index < len(messages):
        msg = messages[index]
    else:
        msg = "Invalid index. Please try between 0 and 4."
    print(f"Accessed: /message/{index} - Served quote by index")
    return render_template_string(css_style + f"<div class='quote'>{msg}</div>")

if __name__ == "__main__":
    app.run(debug=True, port=5000)