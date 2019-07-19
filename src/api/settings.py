#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-16 16:34:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


HEADER = {
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Headers": "content-type",
    "Access-Control-Allow-Methods": "GET,HEAD,PUT,PATCH,POST,DELETE",
    "Access-Control-Allow-Origin": "*",
}


class ResourceMixin(object):
    """docstring for ResourceMixin"""

    def __init__(self):
        self.header = HEADER

    def options(self, *args, **kwargs):
        return '', 200, self.header
