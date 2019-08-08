#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-19 21:52:04
# @Author  : Shanming (shanming0428@163.com)
# @Version : 1.0.0

from flask import render_template, redirect, url_for
from . import record
from .. import db
from ..models import Record, User, Course

from .forms import RegisterForm
from .. import helper


@record.route('/')
def index():
    pagination, fields = helper.fetch_pagination(Record)
    return render_template('record_list.html',
                           pagination=pagination,
                           fields=fields)


@record.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    form.user_id.choices = [(user.id, user.name) for user in User.query.all()]
    form.course_id.choices = [(course.id, course.name)
                              for course in Course.query.all()]
    if form.validate_on_submit():
        record = Record.query.filter_by(user_id=form.user_id.data,
                                        course_id=form.course_id.data,
                                        logged=form.logged.data).first()
        if not record:
            record = helper.form_to_model(form, Record)
            db.session.add(record)
            db.session.commit()
        return redirect(url_for('.index'))

    return render_template('_register.html',
                           form=form)


@record.route('/<int:inst_id>', methods=['GET', 'POST'])
def edit(inst_id):
    form = RegisterForm()
    form.user_id.choices = [(user.id, user.name) for user in User.query.all()]
    form.course_id.choices = [(course.id, course.name)
                              for course in Course.query.all()]
    record = Record.query.get(inst_id)
    if not record:
        return render_template('404.html')
    if form.validate_on_submit():
        record = helper.form_to_model(form, Record)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('.index'))
    else:
        form = helper.model_to_form(record, form)
        return render_template('_edit.html',
                               form=form)
