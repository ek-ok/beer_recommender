#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Initialize the view package
"""

from recommender import application
from .rec import rec
from flask import render_template


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404