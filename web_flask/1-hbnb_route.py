#!/usr/bin/python3
"""This module starts a simple Flask web application"""

from flask import Flask

app = Flask(__name__)

def hbnb_hello():
    """ Display "Hello HBNB!" when visiting the route URL """
    return 'Hello HBNB!'

def hbnb():
    """ Displays "HBNB" when visiting the /hbnb URL """
    return 'HBNB'

@app.route('/', strict_slashes=False)
def hbnb_hello_route():
    """ Route to display Hello HBNB! """
    return hbnb_hello()

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ Route to display HBNB """
    return hbnb()


if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)
