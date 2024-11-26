from flask import render_template, redirect, url_for, session, flash
from finalproject import app, mysql
from finalproject.fvalidation import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import html

# Register Page Route
@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        cursor = mysql.connection.cursor()
        
        cursor.execute("SELECT * FROM users WHERE email = %s", [form.email.data])
        user = cursor.fetchone()
        
        if user:
            return render_template('register.html', title="Register", form=form, error="Email already registered.")
    
        sanitized_username = html.escape(form.username.data)
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')

        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                       (sanitized_username, form.email.data, hashed_password))
        mysql.connection.commit()
        cursor.close()
        
        return redirect(url_for('login'))
    
    return render_template('register.html', title="Register", form=form)

# Login Page Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE email = %s", [form.email.data])
            user = cursor.fetchone()
            cursor.close()

            if user and check_password_hash(user[3], form.password.data):
                session['user_id'] = user[0]
                session['username'] = user[1]
                flash('Login successful!', 'success')
                return redirect(url_for('homepage'))
            else:
                flash('Invalid email or password.', 'error')
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')

    return render_template('login.html', title="Login", form=form)


# Homepage Route
@app.route('/homepage')
def homepage():
    if 'user_id' not in session:
        return redirect(url_for('login')) 
    return render_template('homepage.html', title="Homepage", username=session['username'])


# About Page Route
@app.route('/about')
def about():
    if 'user_id' not in session:
        return redirect(url_for('login'))  
    return render_template('about.html', title="About Us")


# Portfolio Page Route
@app.route('/portfolio')
def portfolio():
    if 'user_id' not in session:
        return redirect(url_for('login')) 
    return render_template('portfolio.html', title="Portfolio")


# Contact Page Route
@app.route('/contact')
def contact():
    if 'user_id' not in session:
        return redirect(url_for('login')) 
    return render_template('contact.html', title="Contact")
