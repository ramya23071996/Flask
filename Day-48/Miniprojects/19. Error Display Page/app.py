from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Ramya's App</h1>"

@app.route("/trigger-error")
def trigger_error():
    raise Exception("Something went wrong!")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html", error_message="Internal server error"), 500

if __name__ == "__main__":
    app.run(debug=True)