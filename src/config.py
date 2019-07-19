#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 11:24:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import pathlib

BASEDIR = pathlib.Path(__file__).parent.parent


class Config():
    pass


class DevelopmentConfig(Config):
    """docstring for DevelopmentConfig"""
    DEBUG = True
    SECRET_KEY = 'A1234567890'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/train_record.db'.format(BASEDIR)


class ProductConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'product': ProductConfig,
    'default': DevelopmentConfig
}
