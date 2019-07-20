#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 10:12:59
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import datetime
from flask_restful import Resource, reqparse

from src.models import Record
from .helper import ResourceObjectMixin, ResourceListMixin

"""
inst_id = db.Column(db.Integer, primary_key=True)
userId = db.Column(db.Integer,
                   db.ForeignKey(User.userId),
                   nullable=False)

courseId = db.Column(db.Integer,
                     db.ForeignKey(Course.courseId),
                     nullable=False)
logged = db.Column(db.DateTime())
comment = db.Column(db.Text())
"""

RecordParser = reqparse.RequestParser()
RecordParser.add_argument('user_id', required=True, help='User ID')
RecordParser.add_argument('course_id', required=True, help='Course ID')
RecordParser.add_argument('logged', type=datetime.datetime,
                          help='Record logged time')
RecordParser.add_argument('comment', help='Record comment')


class RecordResource(Resource, ResourceObjectMixin):
    model_class = Record
    request_parser = RecordParser


class RecordListResource(Resource, ResourceListMixin):
    model_class = Record
    request_parser = RecordParser
