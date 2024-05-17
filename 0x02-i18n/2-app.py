#!/usr/bin/env python3
""" Python script that starts a Flask web application """

from flask import Flask, render_template, request

app = Flask(__name__)

app.config['LANGUAGES'] = ['en', 'fr']


def get_locale():
    """ Function that determining the user's preferred language and local"""

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Function that returns the index.html template """
    locale_user = get_locale()
    return render_template('2-index.html', user_local=locale_user)


if __name__ == "__main__":
    app.run(debug=True)
