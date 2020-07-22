# This is where the configuration files will come... I'm personally not comfortable with the config.py yet
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv
from pathlib import Path
from flask_mail import Mail

env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)

login_manager = LoginManager()
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)

login_manager.login_view = "login"
