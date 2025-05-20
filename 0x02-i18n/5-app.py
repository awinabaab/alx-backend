#!/usr/bin/env python3
"""Basic flask-babel setup"""

from flask import Flask, render_template, request, g
from flask.typing import ResponseReturnValue
from flask_babel import Babel, gettext
from typing import Union, Dict


class Config:
    """Flask app configuration class"""

    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"

    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"}
}


def get_user(login_as=None) -> Union[Dict, None]:
    """Returns the requested user object"""
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request() -> None:
    """Get user and set it as a global on flask.g"""
    login_as = request.args.get("login_as")
    user = get_user(login_as)
    if user:
        g.user = user
        setattr(app.config, "BABEL_DEFAULT_LOCALE", user.get('locale'))


@babel.localeselector
def get_locale() -> str:
    """Determines the best match with the supported languages"""
    locale = request.args.get('locale')
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index() -> ResponseReturnValue:
    """Renders and returns 5-index.html"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
