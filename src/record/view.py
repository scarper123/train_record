#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-19 21:52:04
# @Author  : Shanming (shanming0428@163.com)
# @Version : 1.0.0

from flask import render_template, redirect, url_for, send_file, request
from . import record
from .. import db
from ..models import Record, User, Course

from .forms import RegisterForm
from .. import helper


@record.route('/')
def index():
    query = None
    q = request.args.get('q')
    if q:
        search = '%{}%'.format(request.args['q'])
        q1 = Record.query.filter(Record.comment.like(search))
        query = q1
    pagination, fields = helper.fetch_pagination(Record, query)
    return render_template('record_list.html',
                           pagination=pagination,
                           fields=fields,
                           search_value=q or "")


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
                           form=form,
                           name="Record")


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
        record = helper.form_to_model(form, record)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('.index'))
    else:
        form = helper.model_to_form(record, form)
        return render_template('_edit.html',
                               form=form,
                               name="Record[%s]" % inst_id)


@record.route('/download', methods=['GET'])
def download():
    return send_file(helper.download_file(Record),
                     mimetype='text/csv',
                     attachment_filename='record.csv',
                     as_attachment=True)
