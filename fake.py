#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 10:50:50
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import os
import random
from faker import Faker

from src import create_app, db
from src.models import User, Course, Record, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


def fakeUser():
    userRole = Role.query.filter_by(name='User').first()
    faker = Faker()
    for inx in range(1, 10):
        name = faker.name()
        user = User(name=name,
                    password=name,
                    role_id=userRole.id)
        db.session.add(user)
    db.session.commit()


def fakeCourse():
    faker = Faker()
    for inx in range(1, 51):
        course = Course(name=faker.name(),
                        tel=faker.phone_number(),
                        website=faker.uri(),
                        desc=faker.text())
        db.session.add(course)

    db.session.commit()


def fakeRecord():
    faker = Faker()
    user_ids = [user.id for user in User.query.all() if user.name != 'admin']
    course_ids = [course.id for course in Course.query.all()]
    for inx in range(1, 51):
        post = Record(user_id=random.choice(user_ids),
                      course_id=random.choice(course_ids),
                      logged=faker.date_time(),
                      comment=faker.text())

        db.session.add(post)

    db.session.commit()


def main():
    with app.app_context():
        db.drop_all()
        db.create_all()

        Role.insert_roles()
        User.insert_users()

        fakeUser()
        fakeCourse()
        fakeRecord()
    app.run(debug=True)


if __name__ == '__main__':
    main()
