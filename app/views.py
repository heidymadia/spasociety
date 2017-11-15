#views.py

from flask import Flask
from flask_restful import Resource, Api, reqparse
import jwt
from werkzeug import generate_password_hash, check_password_hash
from app import app, api, mysql, conn, cursor

"""
Landing Page
"""
@app.route('/')
def hello():
    return 'Hello, World!';
