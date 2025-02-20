#!/usr/bin/python3
"""
This is the ``task_04_flask`` module
"""
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Handle root URL"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Display data"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Display Status"""
    return "OK"


@app.route('/users/<username>')
def userInfo(username):
    """Display specified user"""
    if username in users:
        return jsonify(users[username])
    error = {"error": "User not found"}
    return jsonify(error), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user"""
    userdata = request.get_json()
    username = userdata.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = userdata
    return jsonify({"message": "User added"}), 201


if __name__ == "__main__":
    app.run(debug=True)
