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
from src.models import User, Course, Record

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


def fakeUser():
    faker = Faker()
    for inx in range(1, 100):
        name = faker.name()
        user = User(name=name)
        db.session.add(user)
    db.session.commit()


def fakeCourse():
    faker = Faker()
    for inx in range(1, 51):
        course = Course(name=faker.name(),
                        desc=faker.text())
        db.session.add(course)

    db.session.commit()


def fakeRecord():
    faker = Faker()
    user_ids = [user.id for user in User.query.all()]
    course_ids = [course.id for course in Course.query.all()]
    for inx in range(1, 51):
        record = Record(user_id=random.choice(user_ids),
                        course_id=random.choice(course_ids),
                        logged=faker.date_time(),
                        comment=faker.text())

        db.session.add(record)

    db.session.commit()


def main():
    with app.app_context():
        db.drop_all()
        db.create_all()

        fakeUser()
        fakeCourse()
        fakeRecord()
    app.run(debug=True)


def db_test():
    import pprint
    with app.app_context():
        user = User.query.first()
        data_dict = {(col, getattr(user, col))
                     for col in user.__table__.columns.keys()}
        pprint.pprint(data_dict)
        pprint.pprint(Record.__table__.columns.keys())


if __name__ == '__main__':
    main()
