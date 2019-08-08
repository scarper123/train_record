#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-08 14:52:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    desc = TextField('Desc')

    submit = SubmitField('Submit')
