from flask import Flask, abort

app = Flask(__name__)

# 1. /hello/<name>
@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}!"

# 2. /square/<int:number>
@app.route('/square/<int:number>')
def square_number(number):
    return f"The square of {number} is {number ** 2}"

# 3. /greet/<name>/<int:age>
@app.route('/greet/<name>/<int:age>')
def greet(name, age):
    return f"Hi {name}, you are {age} years old."

# 4. /status/<username>/<status>
@app.route('/status/<username>/<status>')
def user_status(username, status):
    return f"{username} is currently {status}."

# 5. /price/<float:amount>
@app.route('/price/<float:amount>')
def show_price(amount):
    return f"The price is ₹{amount:.2f}"

# 6. /profile/<username>
@app.route('/profile/<username>')
def profile(username):
    return f"""
    <html>
        <body>
            <h2>Profile</h2>
            <p>Username: {username}</p>
            <p>Status: Active</p>
        </body>
    </html>
    """

# 7. /math/<int:x>/<int:y>
@app.route('/math/<int:x>/<int:y>')
def math_operations(x, y):
    return f"Sum: {x + y}, Difference: {x - y}, Product: {x * y}"

# 8. /file/<path:filename>
@app.route('/file/<path:filename>')
def file_path(filename):
    return f"Requested file path: {filename}"

# 9. /color/<string:color>
@app.route('/color/<string:color>')
def color_text(color):
    return f'<p style="color:{color};">This is {color} text!</p>'

# 10. /language/<lang>
@app.route('/language/<lang>')
def check_language(lang):
    supported = ['python', 'java', 'c++', 'javascript']
    if lang.lower() in supported:
        return f"{lang.title()} is supported."
    else:
        return f"{lang.title()} is not supported."

# 11. /checkuser/<username>
@app.route('/checkuser/<username>')
def check_user(username):
    valid_users = ['alice', 'bob', 'charlie']
    if username.lower() in valid_users:
        return f"Welcome back, {username}!"
    else:
        return "User not found", 404

# 12. /country/<code>
@app.route('/country/<code>')
def country_name(code):
    countries = {
        'IN': 'India',
        'US': 'United States',
        'UK': 'United Kingdom',
        'FR': 'France'
    }
    return countries.get(code.upper(), 'Country code not recognized')

# 13. Debug print
@app.route('/debug/<info>')
def debug_print(info):
    print(f"Debug: Received parameter '{info}'")  # Will show in console
    return f"Check console for debug info: {info}"

# 14. HTML with triple quotes
@app.route('/html/<title>/<content>')
def html_page(title, content):
    return f"""
    <html>
        <head><title>{title}</title></head>
        <body>
            <h1>{title}</h1>
            <p>{content}</p>
        </body>
    </html>
    """

# 15. /error/<code>
@app.route('/error/<int:code>')
def error_code(code):
    error_messages = {
        404: "Page Not Found",
        500: "Internal Server Error",
        403: "Forbidden",
        401: "Unauthorized"
    }
    return error_messages.get(code, "Unknown Error"), code


if __name__ == '__main__':
    app.run(debug=True)
