#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Start this web app
"""

from recommender import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)