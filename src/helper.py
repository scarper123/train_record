#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-09 14:13:04
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import csv
import pathlib
import inspect

BASEDIR = pathlib.Path(__file__).parent.parent

PER_PAGE = 10


def form_to_model(form, model):
    if inspect.isclass(model):
        model = model()

    for k, v in form.data.items():
        if hasattr(model, k):
            setattr(model, k, v)

    return model


def model_to_form(model, form):
    for k in form.data.keys():
        if hasattr(model, k):
            setattr(getattr(form, k), 'data', getattr(model, k))
    return form


def fetch_pagination(model_cls):
    pagination = model_cls.query.paginate(per_page=PER_PAGE)
    fields = getattr(model_cls, 'fields', model_cls.__table__.columns.keys())
    exclude_fields = getattr(model_cls, 'exclude_fields', [])
    for ext in exclude_fields:
        fields.remove(ext)

    return pagination, fields


def download_file(model_cls):
    all_data = map(lambda x: x.to_dict(), model_cls.query.all())
    fields = model_cls.query.first().to_dict().keys()
    output_dir = BASEDIR / 'output'
    if not output_dir.exists():
        output_dir.mkdir()
    output_file = output_dir / '{}.csv'.format(model_cls.__name__)

    with output_file.open('wt') as f:
        writer = csv.DictWriter(f,
                                dialect='unix',
                                fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_data)

    return str(output_file)
