#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Instantiate flask app and
resister blueprints
"""


from flask import Flask
import os
from recommender.config import ProdConfig
from recommender.config import DevConfig

app = Flask(__name__)

if os.uname()[1] == 'MacBookPro.local':
    app.config.from_object(DevConfig)
else:
    app.config.from_object(ProdConfig)

from recommender.views.main import main
from recommender.views.rec import rec
from recommender.views.analysis import anal

app.register_blueprint(main)
app.register_blueprint(rec, url_prefix='/recommend')
app.register_blueprint(anal, url_prefix='/analysis')
