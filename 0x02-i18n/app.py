#!/usr/bin/env python3
"""7-app module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """config for babel & app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id: int):
    """get user by id"""
    if users.get(id):
        return users.get(id)
    else:
        return None


@babel.localeselector
def get_locale():
    """to determine the best match with our supported languages."""
    locales = Config.LANGUAGES
    lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    loc = request.args.get('locale')

    if loc in locales:
        lang = loc

    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in locales:
            lang = user_locale

    if request.headers.get('locale'):
        if request.headers.get('locale') in locales:
            lang = request.headers.get('locale')

    return lang


@babel.timezoneselector
def get_timezone():
    """
    Select and return appropriate timezone
    """
    tzone = request.args.get('timezone')
    print(tzone)
    if tzone:
        try:
            return timezone(tzone).zone
        except UnknownTimeZoneError:
            pass
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except UnknownTimeZoneError:
            pass
    default_tz = Config.BABEL_DEFAULT_TIMEZONE
    return default_tz


@app.before_request
def before_request():
    """before request function """
    try:
        login_as = int(request.args.get('login_as'))
        g.user = get_user(login_as)
        time_now = pytz.utc.localize(datetime.utcnow())
        time = time_now.astimezone(timezone(get_timezone()))
        locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
        fmt = "%b %d, %Y %I:%M:%S %p"
        g.time = time.strftime(fmt)
        print(g.time)
    except Exception as err:
        return None


@app.route('/')
def index():
    """
    7-app.py default translation
    """
    return render_template('/index.html')
