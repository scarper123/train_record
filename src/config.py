#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 11:24:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import pathlib

BASEDIR = pathlib.Path(__file__).parent.parent


class Config():
    SECRET_KEY = 'A1234567890'


class DevelopmentConfig(Config):
    """docstring for DevelopmentConfig"""
    DEBUG = True
    DB_FILE = '{}/train_record_dev.db'.format(BASEDIR)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_FILE)


class ProductConfig(Config):
    DB_FILE = '{}/train_record.db'.format(BASEDIR)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_FILE)


config = {
    'development': DevelopmentConfig,
    'product': ProductConfig,
    'default': DevelopmentConfig
}
