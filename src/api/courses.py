#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 10:13:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from flask_restful import Resource, reqparse

from src.models import Course
from .helper import ResourceObjectMixin, ResourceListMixin

"""
inst_id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(64), nullable=False, unique=True)
tel = db.Column(db.String(64))
website = db.Column(db.String(64))
desc = db.Column(db.Text())
"""

CourseParser = reqparse.RequestParser()
CourseParser.add_argument('name', required=True, help='Course name')
CourseParser.add_argument('tel', required=True, help='Course telphone')
CourseParser.add_argument('website', help='Course website')
CourseParser.add_argument('desc', help='Course comment')


class CourseResource(Resource, ResourceObjectMixin):
    model_class = Course
    request_parser = CourseParser


class CourseListResource(Resource, ResourceListMixin):
    """docstring for UserList"""
    model_class = Course
    request_parser = CourseParser
