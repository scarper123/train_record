#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 11:26:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from .api import registerApiResource
    registerApiResource(app)

    return app
