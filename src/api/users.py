#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 10:12:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask_restful import Resource, abort, reqparse

from src.models import User
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

UserParser = reqparse.RequestParser()
UserParser.add_argument('name', help='User name')
UserParser.add_argument('password', help='User password')
UserParser.add_argument('role_id', help='User role id')
UserParser.add_argument('email', help='User email')


def update_user(args, user=None):
    if user is None:
        user = User(vars(args))
    else:
        for name, value in vars(args).items():
            setattr(user, name, value)
    return user


def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, 'User[%r] not exist' % user_id)
    return user


class UserResource(Resource, ResourceMixin):
    def get(self, user_id):
        user = get_user_by_id(user_id)
        return user.to_json(), 200, self.header

    def delete(self, user_id):
        user = get_user_by_id(user_id)
        db.session.delete(user)
        db.session.commit()

        return user.to_json(), 200, self.header

    def put(self, user_id):
        user = get_user_by_id(user_id)
        args = UserParser.parse_args()

        user = update_user(args, user)

        db.session.merge(user)
        db.session.commit()

        return user.to_json(), 201, self.header


class UserListResource(Resource, ResourceMixin):
    """docstring for UserList"""

    def get(self):
        user_list = [user.to_json() for user in User.query.all()]
        return user_list, 200, self.header

    def post(self):
        args = UserParser.parse_args()

        user = update_user(args, None)
        db.session.add(user)
        db.session.commit()

        return user.to_json(), 201, self.header
