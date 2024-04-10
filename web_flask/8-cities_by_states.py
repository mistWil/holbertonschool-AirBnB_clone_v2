#!/usr/bin/python3


"""
Script that starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models import *
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """
    Removes the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Displays an HTML page with a list of all State objects and their cities
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
