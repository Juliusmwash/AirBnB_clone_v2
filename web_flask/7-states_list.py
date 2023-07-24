#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


def fetch_states_cities():
    """Fetch all states with their cities from the storage engine."""
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    for state in states:
        if storage.__class__.__name__ == "DBStorage":
            cities = sorted(state.cities, key=lambda city: city.name)
        else:
            cities = sorted(state.cities, key=lambda city: city.name)
        setattr(state, "cities", cities)
    return states


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display the HTML page with states and their cities."""
    states = fetch_states_cities()
    return render_template('cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_session(exception=None):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
