#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 10:12:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask_restful import Resource, abort, reqparse

from src.models import Role
from src import db
from .settings import ResourceMixin

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


def update_role(args, role=None):
    if role is None:
        role = Role(vars(args))
    else:
        for name, value in vars(args).items():
            setattr(role, name, value)
    return role


def get_role_by_id(role_id):
    role = Role.query.get(role_id)
    if not role:
        abort(404, 'Role[%r] not exist' % role_id)
    return role


class RoleResource(Resource, ResourceMixin):
    def get(self, role_id):
        role = get_role_by_id(role_id)
        return role.to_json(), 200, self.header

    def delete(self, role_id):
        role = get_role_by_id(role_id)
        db.session.delete(role)
        db.session.commit()

        return role.to_json(), 200, self.header

    def put(self, role_id):
        role = get_role_by_id(role_id)
        args = RoleParser.parse_args()

        role = update_role(args, role)

        db.session.merge(role)
        db.session.commit()

        return role.to_json(), 201, self.header


class RoleListResource(Resource, ResourceMixin):
    """docstring for roleList"""

    def get(self):
        role_list = [role.to_json() for role in Role.query.all()]
        return role_list, 200, self.header

    def post(self):
        args = RoleParser.parse_args()

        role = update_role(args, None)
        db.session.add(role)
        db.session.commit()

        return role.to_json(), 201, self.header
