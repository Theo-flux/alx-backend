#!/usr/bin/env python3
"""1-app module"""
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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    1-app.py default translation
    """
    return render_template('/2-index.html')
