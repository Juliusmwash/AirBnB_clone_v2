#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route: /
    Method: GET
    Description: Displays "Hello HBNB!" when the root URL is accessed.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route: /hbnb
    Method: GET
    Description: Displays "HBNB" when /hbnb is accessed.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route: /c/<text>
    Method: GET
    Description: Displays "C " followed by the value of the
    text variable (replace underscores with spaces).

    Parameters:
        text (str): The text to display after "C ".
    """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route: /python/ or /python/<text>
    Method: GET
    Description: Displays "Python " followed by the value of
    the text variable (replace underscores with spaces).
    If no text is provided, it displays "Python is cool".

    Parameters:
        text (str, optional): The text to display after "Python ".
    """
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
