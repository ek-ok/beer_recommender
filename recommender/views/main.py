#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Defines the main view
"""

from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='/../templates')

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    import os
    import application
    envs = os.environ
    server = application.config['DB_SERVER']

    return render_template('about.html', envs=envs, server=server)
