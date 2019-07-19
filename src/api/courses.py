#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 10:13:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
from flask_restful import Resource, abort, reqparse

from src.models import Course
from src import db
from .settings import ResourceMixin

"""
course_id = db.Column(db.Integer, primary_key=True)
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


def update_course(args, course=None):
    if course is None:
        course = Course(vars(args))
    else:
        for name, value in vars(args).items():
            setattr(course, name, value)
    return course


def get_course_by_id(course_id):
    course = Course.query.get(course_id)
    if not course:
        abort(404, 'Course[%r] not exist' % course_id)
    return course


class CourseResource(Resource, ResourceMixin):
    def get(self, course_id):
        course = get_course_by_id(course_id)
        return course.to_json(), 200, self.header

    def delete(self, course_id):
        course = get_course_by_id(course_id)
        db.session.delete(course)
        db.session.commit()
        return course.to_json(), 204, self.header

    def put(self, course_id):
        course = get_course_by_id(course_id)
        args = CourseParser.parse_args()

        course = update_course(args, course)

        db.session.merge(course)
        db.session.commit()

        return course.to_json(), 201, self.header


class CourseListResource(Resource, ResourceMixin):
    """docstring for UserList"""

    def get(self):
        course_list = [course.to_json() for course in Course.query.all()]
        return course_list, 200, self.header

    def post(self):
        args = CourseParser.parse_args()

        course = update_course(args, None)
        db.session.add(course)
        db.session.commit()

        return course.to_json(), 201, self.header
