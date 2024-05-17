#!/usr/bin/python3
"""
First Flask web application module
This module creates a simple Flask web application that returns
a "Hello HBNB!" message on the home page.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """
    Serves as the home page
    Returns:
        str: The string "Hello HBNB!"
    """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """
    Running the Flask application
    """
    app.run(host='0.0.0.0', port=5000)

