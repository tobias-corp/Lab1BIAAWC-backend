"""
A simple Flask app for greeting users and serving static files of frontend.
"""

import os
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders a simple greeting to the user.
    """
    return 'Hello, World!'


@app.route('/greet/<name>')
def greet(name):
    """
    Renders a personalized greeting to the user.
    """
    return 'Hello, {}!'.format(name)


@app.route('/static/<path:path>')
def serve_static(path):
    """
    Serves a static frontend file from the 'static' directory.
    """
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, 'static'), path)
