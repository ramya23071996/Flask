from flask import Flask, request, escape

app = Flask(__name__)

# 1. /search?keyword=flask
@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    if keyword:
        return f"Search results for: {escape(keyword)}"
    return "No keyword found"

# 2. /filter?type=shirt&color=blue&size=M
@app.route('/filter')
def filter_items():
    type_ = request.args.get('type')
    color = request.args.get('color')
    size = request.args.get('size')
    return f"Filtering: Type={type_}, Color={color}, Size={size}"

# 3. Already handled in /search with fallback message

# 4. /params – loop through all query params
@app.route('/params')
def params():
    items = "".join([f"<li>{escape(k)}: {escape(v)}</li>" for k, v in request.args.items()])
    return f"<ul>{items}</ul>"

# 5. /greet?name=John
@app.route('/greet')
def greet_query():
    name = request.args.get('name', 'Guest')
    return f"Hello, {escape(name)}!"

# 6. /profile?mode=admin
@app.route('/profile')
def profile_mode():
    mode = request.args.get('mode', 'user')
    return f"Profile mode: {escape(mode)}"

# 7. /count-params – show number of query parameters
@app.route('/count-params')
def count_params():
    count = len(request.args)
    return f"Number of query parameters: {count}"

# 8. /table – format query params into HTML table
@app.route('/table')
def table():
    rows = "".join([f"<tr><td>{escape(k)}</td><td>{escape(v)}</td></tr>" for k, v in request.args.items()])
    return f"""
    <table border="1">
        <tr><th>Key</th><th>Value</th></tr>
        {rows}
    </table>
    """

# 9. /debug-check?debug=true
@app.route('/debug-check')
def debug_check():
    debug = request.args.get('debug')
    if debug == 'true':
        return "🔍 Debug mode is ON"
    return "Debug mode is OFF"

# 10. /display/<username>?theme=dark
@app.route('/display/<username>')
def display(username):
    theme = request.args.get('theme', 'default')
    return f"User: {escape(username)}<br>Theme: {escape(theme)}"

if __name__ == '__main__':
    app.run(debug=True)