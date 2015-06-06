#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Defines the recommend view
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from recommender import db

anal = Blueprint('anal', __name__, template_folder='/../templates')

@anal.route('/')
def index():
    return render_template('recommend.html', active_page='analysis')