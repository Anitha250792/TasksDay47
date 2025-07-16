from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Task 7: Print method in console for every request
@app.before_request
def log_method():
    print(f"HTTP Method: {request.method}")

# Task 1: Return current method
@app.route('/method-check', methods=['GET', 'POST'])
def method_check():
    return f"Current HTTP Method: {request.method}"

# Task 2: POST only route
@app.route('/submit', methods=['POST'])
def submit():
    return "Data submitted successfully via POST!"

# Task 3: Accept both GET and POST
@app.route('/both-methods', methods=['GET', 'POST'])
def both_methods():
    return f"You used {request.method} method."

# Task 4: Display login form with POST method
# Task 5: On submission, show entered username
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return f"Welcome, {username}!"
    return '''
        <form method="POST">
            Username: <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
    '''

# Task 6: Admin GET only, warn on POST
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        return "POST not allowed on /admin", 405
    return "Welcome to the admin page (GET only)"

# Task 8: Feedback form with textarea
@app.route('/feedback', methods=['GET'])
def feedback_form():
    return '''
        <form method="POST" action="/submit-feedback">
            <textarea name="feedback" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Submit Feedback">
        </form>
    '''

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form.get("feedback")
    return f"Feedback received: {feedback}"

# Task 9: Button to send POST request
@app.route('/post-button', methods=['GET'])
def post_button():
    return '''
        <form method="POST" action="/submit">
            <input type="submit" value="Send POST Request">
        </form>
    '''

# Task 10: Form with GET and POST for comparison
@app.route('/compare-methods', methods=['GET', 'POST'])
def compare_methods():
    output = ''
    if request.method == 'POST':
        output = f"POST Method Received: {request.form.get('data')}"
    elif request.method == 'GET' and 'data' in request.args:
        output = f"GET Method Received: {request.args.get('data')}"
    return f'''
        <form method="GET">
            Enter something (GET): <input name="data">
            <input type="submit" value="Send GET">
        </form>
        <form method="POST">
            Enter something (POST): <input name="data">
            <input type="submit" value="Send POST">
        </form>
        <p>{output}</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
