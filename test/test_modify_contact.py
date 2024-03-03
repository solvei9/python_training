from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Petr", lastname="Ivanov", nickname="pivan", title="developer",
                               company="DevCompany", address="Moscow", mobile="+7 933 933 4545", email="petrov@mail.ru",
                               bday="5", bmonth="August", byear="1976"))
    app.session.logout()