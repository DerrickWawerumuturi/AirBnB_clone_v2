#!/usr/bin/python3
"routes to / and  /hbnb"

from flask import Flask

app = Flask(__name__)

@app.get('/', strict_slashes=False)
def hello():
    """
    string to return when on / route
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hello_world():
    """
    show  on /hbnb
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def variable(text):
    """
    replace _ from the text with a space 
    return C together with the next
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text(text="is cool"):
    """
    replace _ in the text with a space
    default of text is 'is cool'
    Return: Python <text>
    """
    text = text.replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    display "n" if n is a integer
    """
    return f"{n} is a number"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)