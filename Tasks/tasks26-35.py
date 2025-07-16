from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    if keyword:
        return f"Search result for: <b>{keyword}</b>"
    else:
        return "No keyword found"

@app.route('/filter')
def filter_items():
    item_type = request.args.get('type', 'N/A')
    color = request.args.get('color', 'N/A')
    size = request.args.get('size', 'N/A')
    return f"<ul><li>Type: {item_type}</li><li>Color: {color}</li><li>Size: {size}</li></ul>"

@app.route('/list')
def list_args():
    items = "".join(f"<li>{k}: {v}</li>" for k, v in request.args.items())
    return f"<ul>{items}</ul>"

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return f"Hello, <b>{name}</b>!"

@app.route('/profile')
def profile():
    mode = request.args.get('mode', 'user')
    return f"Profile page in <b>{mode}</b> mode"

@app.route('/count')
def count_params():
    count = len(request.args)
    return f"Total query parameters: <b>{count}</b>"

@app.route('/table')
def show_table():
    table_html = "<table border=1><tr><th>Key</th><th>Value</th></tr>"
    for key, value in request.args.items():
        table_html += f"<tr><td>{key}</td><td>{value}</td></tr>"
    table_html += "</table>"
    return table_html

@app.route('/check_debug')
def check_debug():
    debug = request.args.get('debug')
    if debug == 'true':
        return "Debug mode is <b>ON</b>"
    return "Debug mode is <b>OFF</b>"

@app.route('/display/<name>')
def display(name):
    extra = ", ".join(f"{k}: {v}" for k, v in request.args.items())
    return f"<h3>Hello, {name}</h3><p>Query Params: {extra or 'None'}</p>"

if __name__ == '__main__':
    app.run(debug=True)
