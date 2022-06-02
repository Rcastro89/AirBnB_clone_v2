#!/usr/bin/python3
"""first module flask"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """function to return message"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_1():
    """function to return message"""
    return "HBNB"


@app.route('/c/<arg>')
def Cisfun(arg):
    """function to return message"""
    return "C " + arg.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')