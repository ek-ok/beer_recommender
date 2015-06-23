#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
This defines config as objects
"""

import os

class Config(object):
    #Flask config
    DEBUG = False
    TESTING = False
    PORT = 8080

    #DB config
    DB_SERVER = os.environ['DB_SERVER']
    DB_USERNAME = os.environ['DB_USERNAME']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_DATABASE = os.environ['DB_DATABASE']
    DB_PORT = os.environ['DB_PORT']


class ProdConfig(Config):
    PORT = 80


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
