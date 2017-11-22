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
                requests.post(
                    "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
                    auth=("api", "YOUR_API_KEY"),
                    data={"from": "genduts_club@yahoo.com",
                          "to": ["genduts_club@yahoo.com"],
                          "subject": "Hello API",
                          "text": "Testing some Mailgun awesomness!"})

                return {
                    'status' : 'OK',
                    'username' : _username,
                    'message' : 'Username created'
                    }
            else:
                return {
                    'status': 'ERR',
                    'message': 'Something gone wrong'
                }


        except Exception as e:
            raise


"""
AuthUser Class
"""
class AuthUser(Resource):
    def post(self):
        try:
            """
            Synchronous Key Auth
            """
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='username for authentication')
            parser.add_argument('password', type=str, help='Password for authentication')
            parser.add_argument('encoded', type=str, help='encoded payload')
            args = parser.parse_args()

            _username = args['username']
            _password = args['password']
            __encoded = args['encoded']
            _hashed_password = generate_password_hash(_password)

            conn = mysql.connect()
            cursor = conn.cursor()
            data = cursor.callproc('sp_AuthenticateUser', (_username, _hashed_password))
            secret = data[0]

            result = jwt.decode(_encoded,  secret, algorithm='HS512')

            if(_username == result.username):
                return {'status' : 200, 'message' : 'authenticated'}
            else:
                return {'status' : 100, 'message' : 'rejected'}
        except Exception as e:
            return {'error': str(e)}

"""
ProfileUser Class
"""
class ProfileUser(Resource):
    def get(self):
        try:
            return {}

        except Exception as e:
            return {'error': str(e)}

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
            return {'error': str(e)}

"""
List Users
"""
class ListUser(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute("SELECT Host, User FROM mysql.user")
            data = cursor.fetchall()

            if(len(data)>0):
                return {'status':200, 'data':data}
            else:
                return {'status':100, 'message':'Authentication failure'}

        except Exception as e:
            return {'error': str(e)}

"""
Endpoint
"""
api.add_resource(CreateUser, '/users/create')
api.add_resource(AuthUser, '/auth')
api.add_resource(ProfileUser, '/users/profile')
api.add_resource(ListUser, '/users/list')
