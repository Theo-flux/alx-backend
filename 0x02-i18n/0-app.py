#!/usr/bin/env python3
"""
0-app.py file
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """0. Basic Flask app

    Returns:
        _type_: _description_
    """
    return render_template('/0-index.html')
