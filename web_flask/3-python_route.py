#!/usr/bin/python3
""" This script starts a simple Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays "Hello HBNB!" when the root URL is visited """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays "HBNB" when visiting the /hbnb URL """
    return 'HBNB'


@app.route('/c/', strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text='is_cool'):
    """
    Display "C " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    Default value of text is "is_cool".
    """
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is_cool'):
    """
    Display "Python " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    Default value of text is "is_cool".
    """
    return 'Python {}'.format(text).replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
