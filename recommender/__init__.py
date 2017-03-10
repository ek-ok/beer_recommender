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

application = Flask(__name__)

if os.uname()[1] == 'MacBookPro.local':
    application.config.from_object(DevConfig)
else:
    application.config.from_object(ProdConfig)

from recommender.views.main import main
from recommender.views.rec import rec
from recommender.views.analysis import anal

application.register_blueprint(main)
application.register_blueprint(rec, url_prefix='/recommend')
application.register_blueprint(anal, url_prefix='/analysis')