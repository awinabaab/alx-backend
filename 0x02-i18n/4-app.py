#!/usr/bin/env python3
"""Basic flask-babel setup"""

from flask import Flask, render_template, request
from flask.typing import ResponseReturnValue
from flask_babel import Babel, gettext
from typing import Union


class Config:
    """Flask app configuration class"""

    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"

    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Determines the best match with the supported languages"""
    locale = request.args.get('locale')
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index() -> ResponseReturnValue:
    """Renders and returns 4-index.html"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
