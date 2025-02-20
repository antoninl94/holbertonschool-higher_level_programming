#!/usr/bin/python3
"""
This is the ``task_05_basic_security`` module
"""
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import get_jwt_identity, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = "chaussette"
jwt = JWTManager(app)
users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """Verify the password passed during login"""
    if username in users and \
       check_password_hash(users[username]["password"], password):
        return username
    else:
        return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def login_required():
    """Ask for login"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login_jwt():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return None
    if username in users and \
       check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def access_login_jwt():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200



if __name__ == '__main__':
    app.run()
