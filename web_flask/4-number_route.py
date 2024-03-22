#!/usr/bin/python3
""" This module is a script that starts a simple Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays "Hello HBNB" when visiting the root URL """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays "HBNB" when visitng /hbnb URL """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text="is_cool"):
    """
    Display “C ”, followed by the value of the text variable
    Replace underscore _ symbols with a space
    """
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text="is_cool"):
    """
    Display “Python ”, followed by the value of the text variable
    Replace underscore _ symbols with a space
    """
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Display “n is a number” only if n is an integer
    """
    return '{:d} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
