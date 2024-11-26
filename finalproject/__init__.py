from flask import Flask
from flask_mysql_connector import MySQ
app = Flask(__name__)

app.config['SECRET_KEY'] = '30a9c161f25a46f1d97998c10bd0b1f8'
app.config['WTF_CSRF_ENABLED'] = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DATABASE'] = 'flask_db'

mysql = MySQL(app)

from finalproject import routes
