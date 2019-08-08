#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 11:26:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from .config import config


db = SQLAlchemy()
nav = Nav()


@nav.navigation()
def top():
    return Navbar('Train',
                  View('Home', 'main.index'),
                  View('Record', 'record.index'),
                  View('Course', 'course.index'),
                  View('User', 'user.index')
                  )


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    Bootstrap(app)
    nav.init_app(app)

    # main blue
    from .main import main as main_blue
    app.register_blueprint(main_blue)

    # User blueprint
    from .user import user as user_blue
    app.register_blueprint(user_blue)

    # Course blueprint
    from .course import course as course_blue
    app.register_blueprint(course_blue)

    # Record blueprint
    from .record import record as record_blue
    app.register_blueprint(record_blue)

    return app
