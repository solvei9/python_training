# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.creat_contact(Contact(firstname="Ivan", lastname="Petrov", nickname="pivan", title="developer",
                              company="DevCompany", address="Moscow", mobile="+7 933 933 4545", email="petrov@mail.ru",
                              bday="5",
                              bmonth="August", byear="1976"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.creat_contact(Contact(firstname="", lastname="", nickname="", title="", company="", address="", mobile="",
                              email="", bday="", bmonth="", byear=""))
    app.logout()
