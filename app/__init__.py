# app/__init__.py

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask.ext.mysql import MySQL
import jwt
from werkzeug import generate_password_hash, check_password_hash


# Initialize the FLASK application
app = Flask(__name__, instance_relative_config=True)

# Flask RESTful API
api = Api(app)

# Flask extention MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'SPASOCIETY_STORE'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

# PyJWT


# Load the views
from app import views

#load the config file
app.config.from_object('config')
