__author__ = 'Xomak'

from flask_hello import app
from flask_hello.dogs import dogs_page

app.register_blueprint(dogs_page, url_prefix='/dogs')