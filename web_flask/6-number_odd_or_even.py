#!/usr/bin/python3


"""Flask web application that defines multiple routes"""


from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Route to display Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """Route to display text with 'C' prefix"""
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route to display text with 'Python' prefix"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Route to display a number.

    Parameters:
    - n (int): The number to be displayed.

    Returns:
    - str: A string representation of the number.
    """
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_htmlpage(n):
    """
    Route to display an HTML page with a number.

    Parameters:
    - n (int): The number to be displayed.

    Returns:
    - str: The rendered HTML page.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """
    Route to display an HTML page with a number and its parity.

    Parameters:
    - n (int): The number to be displayed.

    Returns:
    - str: The rendered HTML page with the number and its parity.
    """
    parity = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
