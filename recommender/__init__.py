#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Instantiate flask app and
resister blueprints
"""


from flask import Flask
from recommender.config import ProdConfig
from recommender.config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

from recommender.views.rec import rec
from recommender.views.main import main
app.register_blueprint(rec, url_prefix='/recommend')
app.register_blueprint(main)