#!/usr/bin/python3
"""first module flask"""

from os import abort
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


@app.route('/python/<arg>')
@app.route('/python/')
def PythonIs(arg='is cool'):
    """function to return message"""
    return "Python " + arg.replace("_", " ")


@app.route('/number/<int:num>')
def Number(num):
    """function to return message"""
    if type(num) is int:
        return str(num) + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
