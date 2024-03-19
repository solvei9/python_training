from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Petrov", nickname="pivan", title="developer",
                                   company="DevCompany", address="Moscow", mobile="+7 933 933 4545",
                                   email="petrov@mail.ru", bday="5", bmonth="August", byear="1976"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
