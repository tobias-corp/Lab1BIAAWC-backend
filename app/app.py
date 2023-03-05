from flask import Flask, send_from_directory
import os

app = Flask(__name__)


@app.route('/')
def index():
    return f'Hello, World!'


@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


@app.route('/static/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, 'static'), path)


if __name__ == '__main__':
    app.run()
