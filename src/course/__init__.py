#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 11:26:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


from flask import Blueprint

course = Blueprint('course', __name__, url_prefix='/courses')

from . import view
