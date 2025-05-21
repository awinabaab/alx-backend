#!/usr/bin/env python3
"""Basic flask-babel setup"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext, format_datetime
from typing import Union, Dict
from datetime import datetime
import pytz


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


@app.context_processor
def inject_formatter() -> Dict:
    """Make format_datetime available to the template context"""
    return dict(format_datetime=format_datetime)


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
    if g and g.get("user"):
        return g.user.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def validate_timezone(timezone: str = None) -> Dict:
    """Determines if timezone in a valid IANA timezone"""
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return None


@babel.timezoneselector
def get_timezone() -> str:
    """Determines if the provided timezone is valid"""
    timezone = request.args.get("timezone")

    if not timezone and g and g.get("user") and g.get("user").get("timezone"):
        timezone = g.user.get("timezone")

    return validate_timezone(timezone)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Renders and returns index.html"""
    return render_template("index.html", current_time=datetime.utcnow())


if __name__ == "__main__":
    app.run()
