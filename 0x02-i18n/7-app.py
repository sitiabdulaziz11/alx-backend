#!/usr/bin/env python3
"""
Simple Flask app with jinja template and flask_babel for i18n
"""


from flask import Flask, g, render_template, request
from flask_babel import Babel
from pytz import timezone, exceptions

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Class for configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Mock user log in """
    user = request.args.get('login_as')
    if user is not None and (user.isnumeric() and
                             int(user) in users.keys()):
        return users[int(user)]
    return None


@app.before_request
def before_request():
    """ Execute get_user before all functions """
    user = get_user()
    if user is not None:
        g.user = user
    else:
        g.user = None


@babel.localeselector
def get_locale():
    """ Get locale from query argument or browser request header """
    locale = request.args.get('locale')
    if locale is not None and locale in app.config["LANGUAGES"]:
        return locale
    elif g.user is not None and g.user["locale"] in app.config["LANGUAGES"]:
        locale = g.user["locale"]
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """ Get timezone """
    time_zone = request.args.get('timezone')
    user_time_zone = g.user["timezone"]
    if time_zone is not None:
        try:
            return timezone(time_zone)
        except exceptions.UnknownTimeZoneError:
            pass
    elif user_time_zone is not None:
        try:
            return timezone(user_time_zone)
        except exceptions.UnknownTimeZoneError:
            pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route("/")
def index():
    """ Function that displays the Jinja template """
    username = None if g.user is None else g.user["name"]
    return render_template('7-index.html', username=username)


if __name__ == '__main__':
    app.run()
