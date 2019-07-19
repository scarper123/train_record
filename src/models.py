#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 11:35:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class Permission():
    VIEW = 1
    EDIT = 2
    CREATE = 4
    MODERATE = 8
    ADMIN = 16


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    desc = db.Column(db.String(64))

    permissions = db.Column(db.Integer)

    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def __str__(self):
        return self.name

    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.VIEW,
                     Permission.EDIT,
                     Permission.CREATE],
            'Moderator': [Permission.VIEW,
                          Permission.EDIT,
                          Permission.CREATE,
                          Permission.MODERATE],
            'Admin': [Permission.VIEW,
                      Permission.EDIT,
                      Permission.CREATE,
                      Permission.MODERATE,
                      Permission.ADMIN],
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)

            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'permissions': self.permissions,
            'desc': self.desc
        }


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128),
                     nullable=False,
                     unique=True,
                     index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(128))
    active = db.Column(db.Boolean(), default=True)

    role_id = db.Column(db.Integer(), db.ForeignKey(Role.id))

    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(128))
    current_login_ip = db.Column(db.String(128))
    login_count = db.Column(db.Integer())

    records = db.relationship('Record',
                              backref='user',
                              lazy=True)

    @property
    def is_active(self):
        return self.active

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Course %r>' % self.name

    @staticmethod
    def insert_users():
        admin_user = User.query.filter_by(name='admin').first()
        if admin_user is None:
            admin_role = Role.query.filter_by(name='Admin').first()
            admin_user = User(name='admin',
                              password='admin',
                              email='admin@email.com',
                              role_id=admin_role.id)
            db.session.add(admin_user)
            db.session.commit()

    def to_json(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'active': self.active,
            'role_id': self.role_id
        }


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),
                     nullable=False,
                     unique=True,
                     index=True)
    tel = db.Column(db.String(128))
    website = db.Column(db.String(128))
    desc = db.Column(db.Text())

    records = db.relationship('Record',
                              backref='course',
                              lazy=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'tel': self.tel,
            'website': self.website,
            'desc': self.desc
        }

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Course %r>' % self.name


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey(User.id),
                        nullable=False)

    course_id = db.Column(db.Integer,
                          db.ForeignKey(Course.id),
                          nullable=False)
    logged = db.Column(db.DateTime())
    comment = db.Column(db.Text())

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'course_id': self.course_id,
            'logged': self.logged.strftime('%Y-%m-%d %H:%M:%S'),
            'comment': self.comment
        }

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<Post %r:%r:%r>' % (self.user.name,
                                    self.course.name,
                                    self.logged)
