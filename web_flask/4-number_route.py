#!/usr/bin/python3
"""a script that starts a Flask web application: """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """  display Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """  display HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """  display C """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text='is cool'):
    """  display python """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """  display n is a number """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
