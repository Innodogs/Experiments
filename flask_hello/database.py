import psycopg2
from flask import g
from flask_hello import app

# from runserver import app

__author__ = 'Xomak'


def connect_db():
    """Connects to the specific database."""
    conn = psycopg2.connect(app.config['DATABASE'])
    return conn


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    print(g)
    if not hasattr(g, 'postgres_db'):
        g.postgres_db = connect_db()
    return g.postgres_db
