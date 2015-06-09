#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Start this web app
"""

from recommender import app as application


if __name__ == '__main__':
    application.run(host='0.0.0.0',
                    port=application.config['PORT'],
                    debug=application.config['DEBUG'])
