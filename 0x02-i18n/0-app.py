#!/usr/bin/env python3
"""Flask app that returns Hello World
"""
from flask import Flask, render_template


app = Flask("__name__")


@app.route('/')
def index():
    """This returns the index page
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
