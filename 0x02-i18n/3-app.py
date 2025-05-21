#!/usr/bin/env python3
"""Basic flask-babel setup"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """Flask app configuration class"""

    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"

    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines the best match with the supported languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index() -> str:
    """Renders and returns 3-index.html"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
