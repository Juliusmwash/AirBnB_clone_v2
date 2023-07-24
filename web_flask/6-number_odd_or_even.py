#!/usr/bin/python3
""" Flask web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route to display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display "HBNB" """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """
    Route to display "C ", followed by the value of the
    text variable (replace underscore _ symbols with a space)
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text="is_cool"):
    """Route to display "Python ", followed by the value of
    the text variable (replace underscore _ symbols with a space)
    The default value of text is "is_cool" """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """
    Route to display "<n> is a number" only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route to display an HTML page only if n is an integer:
    The HTML page contains an H1 tag with the content
        "Number: n"
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route to display an HTML page only if n is an integer:
    The HTML page contains an H1 tag with the content
        "Number: n is even|odd"
    """
    if isinstance(n, int):
        odd_or_even = "odd" if n % 2 else "even"
        return render_template(
                '6-number_odd_or_even.html',
                n=n, odd_or_even=odd_or_even)


if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
