#!/usr/bin/env python3
""" Flask App Module"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel()


class Config(object):
    """ Flask Config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel.init_app(app)


@app.route('/')
def index():
    """ Index Page Method"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
