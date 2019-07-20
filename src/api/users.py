#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 10:12:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask_restful import Resource, reqparse

from src.models import User
from .helper import ResourceObjectMixin, ResourceListMixin

"""
name = db.Column(db.String(64), nullable=False, unique=True)
gender = db.Column(db.Enum('male', 'female'))
birthday = db.Column(db.DateTime())
phone = db.Column(db.String(64))
email = db.Column(db.String(64))
website = db.Column(db.String(64))
"""

UserParser = reqparse.RequestParser()
UserParser.add_argument('name', help='User name')
UserParser.add_argument('password', help='User password')
UserParser.add_argument('role_id', help='User role id')
UserParser.add_argument('email', help='User email')


class UserResource(Resource, ResourceObjectMixin):
    model_class = User
    request_parser = UserParser


class UserListResource(Resource, ResourceListMixin):
    """docstring for UserList"""
    model_class = User
    request_parser = UserParser
