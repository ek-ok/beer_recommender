#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Database connection using pandas
"""

from recommender import application
import pg8000


def fetch_data(query):
    conn = pg8000.connect(host=application.config['DB_SERVER'],
                          port=application.config['DB_PORT'],
                          database=application.config['DB_DATABASE'],
                          user=application.config['DB_USERNAME'],
                          password=application.config['DB_PASSWORD'])

    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
