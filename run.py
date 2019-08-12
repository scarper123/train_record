#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 11:26:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from src import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'product')


@app.before_first_request
def create_firstly():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app.run()
