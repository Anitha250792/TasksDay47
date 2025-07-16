from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Task 1, 2, 3, 4, 5, 6
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()

        # Task 4: Validation
        if not name or not message:
            error = "Both name and message are required."
            return render_template('contact.html', error=error, name=name, message=message)

        # Task 8: Print to terminal
        print(f"[CONTACT FORM] Name: {name}, Message: {message}")

        return redirect(url_for('thank_you', name=name, message=message))

    return render_template('contact.html')


@app.route('/thankyou')
def thank_you():
    name = request.args.get('name', 'Guest')
    message = request.args.get('message', '')
    return render_template('thankyou.html', name=name, message=message)

# Task 7: Feedback form with rating
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name', '')
        rating = request.form.get('rating', '')
        feedback = request.form.get('feedback', '')
        print(f"[FEEDBACK] {name} rated {rating}/5: {feedback}")
        return f"Thank you for your feedback, {name}!"

    return render_template('feedback.html')


# Task 9 & 10: Register form and show data as JSON-like dictionary
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            "name": request.form.get('name', ''),
            "email": request.form.get('email', ''),
            "password": request.form.get('password', '')
        }
        print(f"[REGISTER] {user_data}")
        return f"<h2>Registered User Data</h2><pre>{user_data}</pre>"

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
