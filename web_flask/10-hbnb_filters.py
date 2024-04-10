#!/usr/bin/python3


"""
Flask Application
"""


from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity
import os

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def close_db(error):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()

@app.route('/hbnb_filters')
def hbnb_filters():
    """
    Displays the main filters HTML page
    """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    amenities = list(storage.all(Amenity).values())
    amenities.sort(key=lambda x: x.name)

    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
