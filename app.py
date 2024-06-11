from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission (e.g., save to database, send email)
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # For now, just print the form data to console
        print(f"Received message from {name} ({email}): {message}")
        return render_template('contact.html', success=True)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
