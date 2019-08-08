#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-08 14:52:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DateField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    user_id = SelectField('User',
                          validators=[DataRequired()],
                          coerce=int)
    course_id = SelectField('Course',
                            validators=[DataRequired()],
                            coerce=int)
    logged = DateField('Logged',
                       validators=[DataRequired()])
    comment = StringField('Comment')

    submit = SubmitField('Register')
