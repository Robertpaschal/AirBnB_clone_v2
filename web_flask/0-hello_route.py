#!/usr/bin/python3
"""This module defines a simple Flask web application"""

from flask import Flask

app = Flask(__name__)


def hello_hbnb():
    """Display "Hello HBNB!" when visiting the root URL."""
    return 'Hello HBNB!'


@app.route('/', strict_slashes=False)
def hello_hbnb_route():
    """ Route to display "Hello HBNB!" """
    return hello_hbnb()


if __name__ == '__main__':
    """ Run the app on 0.0.0.0, port 5000."""
    app.run(host='0.0.0.0', port=5000)
