#!/usr/bin/env python3
"""4-app module"""
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
    loc = request.args.get('locale')

    if loc in Config.LANGUAGES:
        lang = loc

    return lang


@app.route('/')
def index():
    """
    4-app.py default translation
    """
    return render_template('/3-index.html')
