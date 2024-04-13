import random

from model.contact import Contact
from random import randrange


def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Ivan", lastname="Petrov", nickname="pivan", title="developer", company="DevCompany",
                    address="Moscow", mobilephone="+7 933 933 4545", email="petrov@mail.ru", bday="5", bmonth="August",
                    byear="1976"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.contact_id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

