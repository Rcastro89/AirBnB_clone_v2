#!/usr/bin/python3
"""first module flask"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(arg):
    """ Handler for teardow"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def lista_estados():
    """ Redirect to page with all states. """
    estados = storage.all("State").values()
    return render_template('7-states_list.html', bum=estados)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
