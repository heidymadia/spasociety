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

"""
CreateUser Class
"""
class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('firstname', type=str, help='First Name to create user')
            parser.add_argument('lastname', type=str, help='Last Name to create user')
            parser.add_argument('username', type=str, help='Username to create user')
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _firstname  = args['firstname']
            _lastname   = args['lastname']
            _username   = args['username']
            _email      = args['email']
            _password   = args['password']
            _hashed_password = generate_password_hash(_password)

            cursor.callproc('spCreateUser',(_firstname,_lastname,_username,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                return {
                    'status' : 'OK',
                    'username' : _username
                    'message' : 'Username created'
                    }
            else:
                return {
                    'status': 'ERR'
                    'message': 'Something gone wrong'
                }


        except Exception as e:
            raise


"""
AuthUser Class
"""
class AuthUser(Resource):
    def post(self):
        jwt decode
        return {'status':'success'}

"""
ProfileUser Class
"""
class ProfileUser(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('firstname', type=str, help='First Name to create user')
            parser.add_argument('lastname', type=str, help='Last Name to create user')
            parser.add_argument('username', type=str, help='Username to create user')
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _firstname  = args['firstname']
            _lastname   = args['lastname']
            _username   = args['username']
            _email      = args['email']
            _password   = args['password']
            _hashed_password = generate_password_hash(_password)

        except Exception as e:
            raise

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('firstname', type=str, help='First Name to create user')
            parser.add_argument('lastname', type=str, help='Last Name to create user')
            parser.add_argument('username', type=str, help='Username to create user')
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _firstname  = args['firstname']
            _lastname   = args['lastname']
            _username   = args['username']
            _email      = args['email']
            _password   = args['password']
            _hashed_password = generate_password_hash(_password)

            return

        except Exception as e:
            raise

"""
Endpoint
"""
api.add_resource(CreateUser, '/users/create')
api.add_resource(AuthUser, '/auth')
api.add_resource(ProfileUser, '/users/profile')
