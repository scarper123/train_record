#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 10:12:59
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import datetime
from flask_restful import Resource, abort, reqparse

from src.models import Record
from src import db
from .settings import ResourceMixin

"""
record_id = db.Column(db.Integer, primary_key=True)
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
RecordParser.add_argument('userId', required=True, help='User ID')
RecordParser.add_argument('courseId', required=True, help='Course ID')
RecordParser.add_argument('logged', type=datetime.datetime,
                          help='Record logged time')
RecordParser.add_argument('comment', help='Record comment')


def update_record(args, record=None):
    if record is None:
        record = Record(vars(args))
    else:
        for name, value in vars(args).items():
            setattr(record, name, value)
    return record


def get_record_by_id(record_id):
    record = Record.query.get(record_id)
    if not record:
        abort(404, 'Record[%r] not exist' % record_id)
    return record


class RecordResource(Resource, ResourceMixin):
    def get(self, record_id):
        record = get_record_by_id(record_id)
        return record.to_json(), 200, self.header

    def delete(self, record_id):
        record = get_record_by_id(record_id)
        db.session.delete(record)
        db.session.commit()

        return record.to_json(), 200, self.header

    def put(self, record_id):
        record = get_record_by_id(record_id)
        args = RecordParser.parse_args()

        record = update_record(args, record)

        db.session.merge(record)
        db.session.commit()

        return record.to_json(), 200, self.header


class RecordListResource(Resource, ResourceMixin):
    """docstring for UserList"""

    def get(self):
        record_list = [record.to_json() for record in Record.query.all()]
        return record_list, 200, self.header

    def post(self):
        args = RecordParser.parse_args()

        record = update_record(args, None)
        db.session.add(record)
        db.session.commit()

        return record.to_json()
