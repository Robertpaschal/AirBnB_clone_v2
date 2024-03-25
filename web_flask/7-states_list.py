#!/usr/bin/python3
""" Script to start a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
import os
app = Flask(__name__)


def import_data():
    """Import data from the 7-dump file """
    try:
        import_path = os.path.abspath('7-dump')
        storage.reload()
        print("Importing data from {}".format(import_path))
    except FileNotFoundError:
        print("Error: 7-dump file not found")


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of all State objects present in DBstorage"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    import_data
    app.run(host='0.0.0.0', port=5000)
