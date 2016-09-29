from flask_hello.database import get_db

__author__ = 'Xomak'

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

dogs_page = Blueprint('dogs', __name__,
                        template_folder='templates')

@dogs_page.route('/', defaults={'page': 'index'})
@dogs_page.route('/<page>')
def show(page):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students;")

        return render_template('index.html', test=str(cursor.fetchone()))
    except TemplateNotFound:
        abort(404)