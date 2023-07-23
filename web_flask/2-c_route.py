#!/usr/bin/python3
""" Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL.

    Returns:
        str: A welcome message "Hello HBNB!".
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for '/hbnb' URL.

    Returns:
        str: A message "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for '/c/<text>' URL.

    Args:
        text (str): The value of the 'text' variable extracted from the URL.

    Returns:
        str: A message "C " followed by the value of the 'text'
        variable with underscores replaced by spaces.
    """
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
