#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Initialize the view package
"""

from recommender import app
from .rec import rec
from flask import render_template


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404