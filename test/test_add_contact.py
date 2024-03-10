# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Ivan", lastname="Petrov", nickname="pivan", title="developer",
                               company="DevCompany", address="Moscow", mobile="+7 933 933 4545", email="petrov@mail.ru",
                               bday="5", bmonth="August", byear="1976"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", nickname="", title="", company="", address="", mobile="",
                               email="", bday="", bmonth="", byear=""))
