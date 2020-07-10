# This is where the configuration files will come... I'm personally not comfortable with the config.py yet
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = b'30724e3ffa2aa2c711423040cd591696'
