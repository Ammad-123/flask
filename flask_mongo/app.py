from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['flask_mongo']  # Database
users = db['users']      # Collection

# Route: Home page
@app.route('/')
def home():
    if 'email' in session:
        return f"Welcome {session['email']}! <br><a href='/logout'>Logout</a>"
    return redirect('/login')

# Route: Register user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        if users.find_one({'email': email}):
            flash('Email already registered. Try logging in.')
            return redirect(url_for('register'))

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Insert new user
        users.insert_one({'email': email, 'password': hashed_password})

        flash('Registration successful! Please login.')
        return redirect(url_for('login'))

    return render_template('register.html')

# Route: Login user
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if the user exists
        user = users.find_one({'email': email})

        if user:
            # Validate the password
            if bcrypt.checkpw(password.encode('utf-8'), user['password']):
                session['email'] = email
                return redirect(url_for('home'))
            else:
                flash('Invalid password!')
        else:
            flash('Email not registered!')

    return render_template('login.html')

# Route: Logout user
@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
