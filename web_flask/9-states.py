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
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
