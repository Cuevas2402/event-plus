from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from flask_session import Session
from flask_socketio import SocketIO
import os

app = Flask(__name__)


load_dotenv('../.env')
app.config['SECRET'] = "secret!123"

socketio = SocketIO(app, cors_allowed_origins = "*")

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') 
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

from app import main_page, credentials, filters, chat, item, cart, profile
