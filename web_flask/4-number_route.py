#!/usr/bin/python3
""" Flask web application """
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route to display 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route to display 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route to display 'C ' followed by the value of the text variable
    (replace underscore _ symbols with a space).
    """
    return "C {}".format(escape(text.replace("_", " ")))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route to display 'Python ' followed by the value of the text variable
    (replace underscore _ symbols with a space).
    """
    return "Python {}".format(escape(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route to display 'n is a number' only if n is an integer.
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
