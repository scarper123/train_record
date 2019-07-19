#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 10:09:56
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from flask_restful import Api
from .users import UserResource, UserListResource
from .courses import CourseResource, CourseListResource
from .records import RecordResource, RecordListResource
from .roles import RoleResource, RoleListResource


def registerApiResource(app):
    api = Api(app, prefix='/api/json')
    api.add_resource(UserResource, '/users/<int:user_id>')
    api.add_resource(UserListResource, '/users')
    api.add_resource(CourseResource, '/courses/<int:course_id>')
    api.add_resource(CourseListResource, '/courses')
    api.add_resource(RecordResource, '/records/<int:record_id>')
    api.add_resource(RecordListResource, '/records')

    api.add_resource(RoleResource, '/roles/<int:role_id>')
    api.add_resource(RoleListResource, '/roles')
