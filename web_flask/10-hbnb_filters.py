#!/usr/bin/python3


"""
Script that starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """
    Removes the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Displays an HTML page with filters for State, City, and Amenity objects
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    cities = storage.all(City).values()
    cities = sorted(cities, key=lambda x: x.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda x: x.name)
    return render_template('10-hbnb_filters.html',
                           states=states, cities=cities, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
