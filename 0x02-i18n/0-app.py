#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template
from flask.typing import ResponseReturnValue


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index() -> ResponseReturnValue:
    """Renders and returns 0-index.html"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
