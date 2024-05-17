#!/usr/bin/python3
"routes to / and  /hbnb"

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

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

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    render html if n is an integer
    """
    return render_template('5-number.html', number=n)

@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """
    display number if either it is odd or even
    """
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", number=n, value="even")
    else:
        return render_template("6-number_odd_or_even.html", number=n, value="odd")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

