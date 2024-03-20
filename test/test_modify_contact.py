from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrov", nickname="pivan", title="developer",
                                   company="DevCompany", address="Moscow", mobile="+7 933 933 4545",
                                   email="petrov@mail.ru", bday="5", bmonth="August", byear="1976"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Petr", lastname="Ivanov", nickname="pivan", title="developer",
                      company="DevCompany", address="Moscow", mobile="+7 933 933 4545",
                      email="petrov@mail.ru", bday="5", bmonth="August", byear="1976")
    contact.contact_id = old_contacts[index].contact_id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrov", nickname="pivan", title="developer",
                                   company="DevCompany", address="Moscow", mobile="+7 933 933 4545",
                                   email="petrov@mail.ru", bday="5", bmonth="August", byear="1976"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(index, Contact(firstname="Mark"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_birthdate(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrov", nickname="pivan", title="developer",
                                   company="DevCompany", address="Moscow", mobile="+7 933 933 4545",
                                   email="petrov@mail.ru", bday="5", bmonth="August", byear="1976"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(index, Contact(bday="10", bmonth="April", byear="1999"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
