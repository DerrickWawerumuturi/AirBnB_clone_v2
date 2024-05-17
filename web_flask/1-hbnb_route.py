#!/usr/bin/python3
"""
Flask web application module with two routes
This module creates a simple Flask web application that returns
specific messages on the home page and the /hbnb route.
"""

from flask import Flask

app = Flask(__name__)

@app.get('/', strict_slashes=False)
def hello():
    """
    Handles the / route
    Returns:
        str: The string "Hello HBNB!"
    """
    return 'Hello HBNB!'

@app.get('/hbnb', strict_slashes=False)
def hello_world():
    """
    Handles the /hbnb route
    Returns:
        str: The string "HBNB"
    """
    return "HBNB"

if __name__ == "__main__":
    """
    Running the Flask application
    """
    app.run(host='0.0.0.0', port=5000)
