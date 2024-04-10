#!/usr/bin/python3


"""
Script that starts a Flask web application
"""


from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """
    Removes the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_and_cities(id=None):
    """
    Displays an HTML page with a list of all State objects
    or a list of cities for a given state
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    if id:
        state = next((state for state in states if state.id == id), None)
        if state:
            cities = sorted(state.cities, key=lambda x: x.name)
            return render_template('9-states.html',
                                   states=states, state=state, cities=cities)
        else:
            return render_template('9-states.html', states=states, state=None)
    else:
        return render_template('9-states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
