#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
This defines config as objects
"""


class Config(object):
    #Flask config
    DEBUG = False
    TESTING = False

    #DB config
    DB_SERVER = 'aws-postgres01.colxr7rvrp2e.us-east-1.rds.amazonaws.com'
    DB_USERNAME = 'user'
    DB_PASSWORD = 'pass'
    DB_DATABASE = 'beer'
    DB_port = 5432

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True
