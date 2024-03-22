#!/usr/bin/python3
""" This module starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_root():
    """ Display "Hello HBNB!" when visiting the root URL. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display "HBNB" when visiting the /hbnb URL. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    Display "C" followed by the value of the text variable.
    Replaces underscore _ symbols with a space.
    """
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    """ Run the app on port 5000 """
    app.run(host='0.0.0.0', port=5000)
