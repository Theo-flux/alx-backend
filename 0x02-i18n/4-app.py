#!/usr/bin/env python3
"""3-app module"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config for babel & app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """to determine the best match with our supported languages."""
    lang = request.accept_languages.best_match(app.config['LANGUAGES'])

    for k, v in request.args.items():
        if k == 'locale':
            if v in Config.LANGUAGES:
                lang = v

    return lang


@app.route('/')
def index():
    """
    3-app.py default translation
    """
    return render_template('/3-index.html')
