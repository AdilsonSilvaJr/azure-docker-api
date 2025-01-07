from flask import jsonify

def hello_world():
    return jsonify(message="Hello, World!")