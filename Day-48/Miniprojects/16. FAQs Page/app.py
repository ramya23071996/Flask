from flask import Flask, render_template

app = Flask(__name__)

@app.route("/faq")
def faq():
    faqs = [
        {"question": "How do I reset my password?", "answer": "Click on 'Forgot Password' and follow the instructions."},
        {"question": "Can I change my username?", "answer": ""},
        {"question": "Where can I find my purchase history?", "answer": "Go to your profile and click 'Orders'."}
    ]
    return render_template("faq.html", faqs=faqs)

if __name__ == "__main__":
    app.run(debug=True)