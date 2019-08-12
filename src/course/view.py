#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-19 21:52:04
# @Author  : Shanming (shanming0428@163.com)
# @Version : 1.0.0

from flask import render_template, redirect, url_for, send_file
from . import course
from .. import db
from ..models import Course
from .forms import RegisterForm

from .. import helper


@course.route('/')
def index():
    pagination, fields = helper.fetch_pagination(Course)
    return render_template('_list.html',
                           pagination=pagination,
                           fields=fields)


@course.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        course = Course.query.filter_by(name=form.name.data).first()
        if not course:
            course = helper.form_to_model(form, Course)
            db.session.add(course)
            db.session.commit()
        return redirect(url_for('.index'))
    return render_template('_register.html',
                           form=form,
                           name="Course")


@course.route('/<int:inst_id>', methods=['GET', 'POST'])
def edit(inst_id):
    form = RegisterForm()
    course = Course.query.get(inst_id)
    if not course:
        return render_template('404.html')
    if form.validate_on_submit():
        course = helper.form_to_model(form, course)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('.index'))
    else:
        form = helper.model_to_form(course, form)
        return render_template('_edit.html',
                               form=form,
                               name="Course[%s]" % inst_id)


@course.route('/download', methods=['GET'])
def download():
    return send_file(helper.download_file(Course),
                     mimetype='text/csv',
                     attachment_filename='course.csv',
                     as_attachment=True)
