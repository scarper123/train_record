#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-19 21:52:04
# @Author  : Shanming (shanming0428@163.com)
# @Version : 1.0.0

from flask import render_template, redirect, url_for
from . import main


@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/')
def home():
    return redirect(url_for('.index'))
