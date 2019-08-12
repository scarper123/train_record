#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-19 21:52:04
# @Author  : Shanming (shanming0428@163.com)
# @Version : 1.0.0

from flask import render_template, redirect, url_for, send_file
from . import user
from .. import db
from ..models import User
from .forms import RegisterForm

from .. import helper


@user.route('/')
def index():
    pagination, fields = helper.fetch_pagination(User)
    return render_template('_list.html',
                           pagination=pagination,
                           fields=fields)


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if not user:
            user = helper.form_to_model(form, User)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('.index'))
    return render_template('_register.html',
                           form=form,
                           name="User")


@user.route('/<int:inst_id>', methods=['GET', 'POST'])
def edit(inst_id):
    form = RegisterForm()
    user = User.query.get(inst_id)
    if not user:
        return render_template('404.html')
    if form.validate_on_submit():
        user = helper.form_to_model(form, user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.index'))
    else:
        form = helper.model_to_form(user, form)
        return render_template('_edit.html',
                               form=form,
                               name="User[%s]" % inst_id)


@user.route('/download', methods=['GET'])
def download():
    return send_file(helper.download_file(User),
                     mimetype='text/csv',
                     attachment_filename='user.csv',
                     as_attachment=True)
