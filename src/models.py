#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 11:35:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from . import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64),
                     nullable=False,
                     unique=True,
                     index=True)
    desc = db.Column(db.String(64))

    records = db.relationship('Record',
                              backref='user',
                              lazy=True)

    # exclude_fields = ['desc']

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc
        }


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),
                     nullable=False,
                     unique=True,
                     index=True)
    desc = db.Column(db.Text())

    records = db.relationship('Record',
                              backref='course',
                              lazy=True)

    # exclude_fields = ['desc']

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc
        }


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey(User.id),
                        nullable=False)

    course_id = db.Column(db.Integer,
                          db.ForeignKey(Course.id),
                          nullable=False)
    logged = db.Column(db.Date())
    comment = db.Column(db.String(128))

    exclude_fields = ['comment']

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.name,
            'course': self.course.name,
            'logged': self.logged,
            'comment': self.comment
        }
