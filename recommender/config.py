#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
This defines config as objects
"""


class Config(object):
    #Flask config
    DEBUG = False
    TESTING = False
    PORT = 8080

    #DB config
    DB_SERVER = 'host'
    DB_USERNAME = 'user'
    DB_PASSWORD = 'pass'
    DB_DATABASE = 'beer'
    DB_PORT = 5432


class ProdConfig(Config):
    PORT = 80


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
