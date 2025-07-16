from flask import Flask

app = Flask(__name__)

@app.route("/calc/<op>/<float:num1>/<float:num2>")
def calculate(op, num1, num2):
    print(f"Accessed: /calc/{op}/{num1}/{num2}")
    
    result = None
    if op == "add":
        result = num1 + num2
    elif op == "sub":
        result = num1 - num2
    elif op == "mul":
        result = num1 * num2
    elif op == "div":
        if num2 == 0:
            return "<h2>Division by zero is not allowed.</h2>"
        result = num1 / num2
    else:
        return "<h2>Invalid operation. Please check /ops for valid options.</h2>"

    return f"""
    <html>
    <head><title>Calculator Result</title></head>
    <body style="font-family:Arial; padding:30px;">
        <h2>Operation: {op}</h2>
        <h2>{num1} {op} {num2} = {result}</h2>
    </body>
    </html>
    """

@app.route("/ops")
def list_ops():
    print("Accessed: /ops")
    return """
    <html>
    <head><title>Supported Operations</title></head>
    <body style="font-family:Verdana; padding:30px;">
        <h2>Valid Operations</h2>
        <ul>
            <li><strong>add</strong> - Addition</li>
            <li><strong>sub</strong> - Subtraction</li>
            <li><strong>mul</strong> - Multiplication</li>
            <li><strong>div</strong> - Division</li>
        </ul>
        <p>Example: <i>/calc/add/12/4</i></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)