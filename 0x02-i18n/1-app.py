#!/usr/bin/env python3
""" Flask App Module"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Flask Config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    app.config.from_object(Config)


@app.route("/")
def index():
    """ Index Page """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
