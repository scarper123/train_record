#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 16:34:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import  json
from flask import  request
from flask_restful import abort
from src import db

HEADER = {
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Headers": "content-type",
    "Access-Control-Allow-Methods": "GET,HEAD,PUT,PATCH,POST,DELETE",
    "Access-Control-Allow-Origin": "*",
}


class ResourceMixin(object):
    """docstring for ResourceMixin"""
    _model_class = None
    _request_parser = None

    def __init__(self):
        self.header = HEADER

    def options(self, *args, **kwargs):
        return '', 200, self.header

    @property
    def model_class(self):
        if not self._model_class:
            raise AttributeError('Lack of model class')
        return self._model_class

    @property
    def request_parser(self):
        if not self._request_parser:
            raise AttributeError('Lack of request parser')
        return self._request_parser


class ResourceObjectMixin(ResourceMixin):
    """docstring for ResourceMixin"""

    def get(self, inst_id):
        inst = get_inst_by_id(self.model_class, inst_id)
        return inst.to_json(), 200, self.header

    def delete(self, inst_id):
        inst = get_inst_by_id(self.model_class, inst_id)
        db.session.delete(inst)
        db.session.commit()
        return inst.to_json(), 204, self.header

    def put(self, inst_id):
        inst = get_inst_by_id(self.model_class, inst_id)
        args = self.request_parser.parse_args()

        inst = update_resource(self.model_class, args, inst)

        db.session.merge(inst)
        db.session.commit()

        return inst.to_json(), 201, self.header


class ResourceListMixin(ResourceMixin):
    """docstring for ResourceListMixin"""

    def get(self):
        args = self.request_parser.parse_args()
        print(args)
        inst_list = self.model_class.query.all()
        inst_list = [inst.to_json() for inst in inst_list]
        return inst_list, 200, self.header

    def post(self):
        args = self.request_parser.parse_args()
        inst = update_resource(self.model_class, args, None)
        db.session.add(inst)
        db.session.commit()

        return inst.to_json(), 201, self.header


def update_resource(model_cls, args, inst=None):
    if inst is None:
        inst = model_cls(vars(args))
    else:
        for name, value in vars(args).items():
            setattr(inst, name, value)
    return inst


def get_inst_by_id(model_cls, inst_id):
    inst = model_cls.query.get(inst_id)
    if not inst:
        abort(404, '%r[%r] not exist' % (model_cls.__name__, inst_id))
    return inst
