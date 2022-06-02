#!/usr/bin/python3
"""first module flask"""

from crypt import methods
from os import abort
from flask import Flask, render_template
from requests import request

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


@app.route('/number_template/<int:num>')
def NumberHtml(num):
    """function to return message"""
    if type(num) is int:
        return render_template('5-number.html', number=num)


@app.route('/number_odd_or_even/<int:num>')
def NumberHtmloddeven(num):
    """function to return message"""
    if type(num) is int:
        tip = 'odd' if num % 2 != 0 else 'even'
        return render_template('6-number_odd_or_even.html',
                               number=num, tipo=tip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
