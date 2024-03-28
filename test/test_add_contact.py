# -*- coding: utf-8 -*-
import pytest
import random
import model.general
from model.contact import Contact

testdata = [
    Contact(firstname=firstname, lastname=lastname, nickname=model.general.random_string("", 9),
                title="developer", company="DevCompany", address="Moscow",
                homephone=model.general.random_phone(), mobilephone=mobilephone, workphone=model.general.random_phone(),
                email=email, email2=model.general.random_email(), email3=model.general.random_email(),
                bday="5", bmonth="August", byear=random.randrange(1900, 2025))
    for firstname in ["", model.general.random_string("Ivan", 5)]
    for lastname in ["", model.general.random_string("Petrov", 3)]
    for mobilephone in ["", model.general.random_phone()]
    for email in ["", model.general.random_email()]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
