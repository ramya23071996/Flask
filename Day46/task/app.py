from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
     print("🔥 Home route accessed!")
     return "Hello, Flask!"  

@app.route('/about')
def about():
    return "This is the about page"  

# 41. Define a /hello route

@app.route('/hello')
def hello():
    return "Welcome to Flask!"

# 42. Dynamic route with <username>
@app.route('/user/<username>')
def show_user(username):
    return f"Hello, {username}!"

 #44. Use different HTTP methods 
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "Form submitted!"
    else:
        return "Displaying form (GET)"
    
# 45. What happens with duplicate route functions?
@app.route('/duplicate')
def one():
    return "First"


@app.route('/duplicate')
def two():
    return "Second"

# 46. Return a basic HTML structure
@app.route('/basic')
def basic_html():
    return "<html><body><h1>Welcome!</h1><p>This is a basic HTML page.</p></body></html>"

# 47. Add inline CSS styling
@app.route('/styled')
def styled_html():
    return "<h1 style='color: blue; font-family: Arial;'>Styled Heading</h1><p style='font-size: 18px;'>This is a styled paragraph.</p>"


# 48. Use Python triple-quoted string to return multiline HTML
@app.route('/multiline')
def multiline_html():
    return """
    <html>
        <head><title>Multiline HTML</title></head>
        <body>
            <h1>Hello from Flask</h1>
            <p>This HTML is returned using a triple-quoted string.</p>
        </body>
    </html>
    """

# 49. Return an unordered list with 3 items
@app.route('/list')
def list_items():
    return """
    <h2>My Favorite Tools</h2>
    <ul>
        <li>Python</li>
        <li>HTML/CSS</li>
        <li>JavaScript</li>
    </ul>
    """

# 50. Use basic HTML tags and explain output
@app.route('/tags')
def show_tags():
    return """
    <h1>Main Heading</h1>
    <p>This is a paragraph explaining things.</p>
    <br>
    <p>New paragraph after line break.</p>
    <hr>
    <p>Section below horizontal line.</p>
    """

if __name__ == '__main__':
    print("🚀 Starting Flask server...")  

    
    app.run(debug=True)


