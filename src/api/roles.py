#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 10:12:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask_restful import Resource, reqparse

from src.models import Role
from .helper import ResourceObjectMixin, ResourceListMixin

"""
name = db.Column(db.String(64), nullable=False, unique=True)
gender = db.Column(db.Enum('male', 'female'))
birthday = db.Column(db.DateTime())
phone = db.Column(db.String(64))
email = db.Column(db.String(64))
website = db.Column(db.String(64))
"""

RoleParser = reqparse.RequestParser()
RoleParser.add_argument('name', help='role name')
RoleParser.add_argument('desc', help='role desc')


class RoleResource(Resource, ResourceObjectMixin):
    model_class = Role
    request_parser = RoleParser


class RoleListResource(Resource, ResourceListMixin):
    """docstring for roleList"""
    model_class = Role
    request_parser = RoleParser
