#!/usr/bin/env python3
""" Python script that starts a Flask web application """

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config['LANGUAGES'] = ['en', 'fr']

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
    """ Function that determining the user's preferred language and local"""
    local = request.args.get('locale')
    if local and local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Function that returns the index.html template """
    locale_user = get_locale()
    return render_template('5-index.html', user_local=locale_user)


if __name__ == "__main__":
    app.run(debug=True)
