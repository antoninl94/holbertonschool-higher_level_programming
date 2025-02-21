#!/usr/bin/python3
"""
This is the ``task_05_basic_security`` module
"""
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import create_access_token, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = "cugiYu645iuh/@jigb"
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
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Ask for login"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """This is the login method"""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and \
       check_password_hash(users[username]['password'], password):
        role = users[username]["role"]
        access_token = create_access_token(identity=username,
                                           additional_claims={"role": role})
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid username or password"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Check for the authorization"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """check for the role during login"""
    claims = get_jwt()
    role = claims.get("role")
    if role != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """handle unauthorized error"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """handle invalid token error"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """handle expired token error"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """handle revoked token error"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """handle fresh token"""
    return jsonify({"error": "Fresh token required"}), 401


@jwt.unauthorized_loader
def handle_missing_token(err):
    """error handling"""
    return jsonify({"error": "Authorization header missing or invalid"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    """error handling"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.invalid_token_loader
def handle_invalid_claims(err):
    """error handling"""
    return jsonify({"error": "Invalid token claims"}), 401


if __name__ == '__main__':
    app.run()
