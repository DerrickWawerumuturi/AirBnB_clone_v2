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

@app.get('/hbnb')
def hello_world():
    """
    show  on /hbnb
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def variable(text):
    text = text.replace('_', ' ')
    return f"C {text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)