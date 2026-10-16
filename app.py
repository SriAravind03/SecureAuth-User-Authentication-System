import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import get_db_connection  # Import database connection function

# Initialize Flask app
app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

# ========================
#        ROUTES
# ========================

# Home Page
@app.route('/')
def index():
    return render_template('index.html')


# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('Email and password are required!', 'danger')
            return redirect(url_for('register'))

        try:
            with get_db_connection() as conn:
                c = conn.cursor()
                
                # Check if user already exists
                c.execute('SELECT * FROM users WHERE email = ?', (email,))
                existing_user = c.fetchone()

                if existing_user:
                    flash('Email already registered. Please log in.', 'danger')
                    return redirect(url_for('login'))

                # Insert new user (Plaintext password - NOT recommended for real applications)
                c.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
                conn.commit()

            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.Error as e:
            flash(f'Database error: {e}', 'danger')

    return render_template('register.html')


# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('Email and password are required!', 'danger')
            return redirect(url_for('login'))

        try:
            with get_db_connection() as conn:
                c = conn.cursor()
                c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
                user = c.fetchone()

            if user:
                session['email'] = email
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials. Please try again.', 'danger')
        except sqlite3.Error as e:
            flash(f'Database error: {e}', 'danger')

    return render_template('login.html')


# Dashboard (Requires Login)
@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash('You must log in first!', 'danger')
        return redirect(url_for('login'))
    return render_template('dashboard.html', email=session['email'])


# Logout Route
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'info')
    return redirect(url_for('index'))


# ========================
#        RUN APP
# ========================
if __name__ == '__main__':
    app.run(debug=True, port=5003)                         