from flask import Flask, render_template, request, redirect, url_for
from phones_data import phones   
from logic import get_listable_phones   

app = Flask(__name__)

# Dummy login credentials
USERNAME = "admin"
PASSWORD = "1234"

# Home page – redirects to login
@app.route('/')
def home():
    return redirect(url_for('login'))

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']

        if user == USERNAME and pw == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid username or password")
    
    return render_template('login.html')

# Dashboard Page – shows all phone listings
@app.route('/dashboard')
def dashboard():
    listed_phones = get_listable_phones(phones)
    return render_template('dashboard.html', phones=listed_phones)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)