#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Database connection using pandas
"""

from recommender import app
import pg8000


def fetch_data(query):
    conn = pg8000.connect(host=app.config['DB_SERVER'],
                          port=app.config['DB_PORT'],
                          database=app.config['DB_DATABASE'],
                          user=app.config['DB_USERNAME'],
                          password=app.config['DB_PASSWORD'])

    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
