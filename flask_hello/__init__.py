from flask import Flask



__author__ = 'Xomak'

app = Flask(__name__)
app.config.from_pyfile("config.cfg")

from flask_hello import blueprints