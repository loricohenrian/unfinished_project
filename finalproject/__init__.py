from flask import Flask
from flask_mysql_connector import MySQL
#__init__.py
app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = '30a9c161f25a46f1d97998c10bd0b1f8'
app.config['WTF_CSRF_ENABLED'] = True

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Update this with your MySQL password if needed
app.config['MYSQL_DATABASE'] = 'flask_db'

# Initialize MySQL
mysql = MySQL(app)

from finalproject import routes  # Import routes after MySQL setup
