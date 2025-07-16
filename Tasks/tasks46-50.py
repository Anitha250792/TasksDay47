from flask import Flask, redirect, url_for, request, render_template_string, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

# Task 1: Redirect /start → /home
@app.route('/start')
def start():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return "<h1>Welcome to the Home Page!</h1>"

# Task 2: Redirect /dashboard → /login if not logged in
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return "<h1>Welcome to your Dashboard</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['logged_in'] = True
        return redirect(url_for('dashboard'))
    return '''
        <h2>Login Page</h2>
        <form method="post">
            <input type="submit" value="Log In">
        </form>
    '''

# Task 3: Dynamic profile URL using url_for
@app.route('/profile/<username>')
def profile(username):
    return f"<h1>Hello, {username.capitalize()}! This is your profile.</h1>"

# Task 4: HTML page with links using url_for inside response string
@app.route('/links')
def links():
    return render_template_string("""
        <h2>Dynamic Links Page</h2>
        <ul>
            <li><a href="{{ url_for('home') }}">Home</a></li>
            <li><a href="{{ url_for('dashboard') }}">Dashboard</a></li>
            <li><a href="{{ url_for('profile', username='mahesh') }}">Mahesh's Profile</a></li>
        </ul>
    """)

# Task 5: Redirect to /thankyou after form submission
@app.route('/submit-form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        return redirect(url_for('thankyou'))
    return '''
        <form method="post">
            <input type="text" name="data" placeholder="Enter something" required>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/thankyou')
def thankyou():
    return "<h1>Thank you for submitting the form!</h1>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
