"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask.ext.mysql import MySQL
import jwt
from werkzeug import generate_password_hash, check_password_hash

"""
Flask Application
"""
app = Flask(__name__)

"""
RESTful Api
"""
api = Api(app)

"""
MySQL
"""
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'SPASOCIETY_STORE'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

"""
JWT
"""


# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

from route import *;


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
    app.run(debug=True);
