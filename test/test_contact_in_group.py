from model.group import Group
from model.contact import Contact
from random import randrange


def test_add_contact_to_group(app, orm):
    groups_list = orm.get_group_list()
    if len(groups_list) == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
        groups_list = orm.get_group_list()
    index = randrange(len(groups_list))
    contacts_not_in_group = orm.get_contacts_not_in_group(groups_list[index])
    if len(contacts_not_in_group) == 0:
        contact = app.contact.create(
            Contact(firstname="Ivan", lastname="Petrov", nickname="pivan", title="developer", company="DevCompany",
                    address="Moscow", mobilephone="+7 933 933 4545", email="petrov@mail.ru", bday="5", bmonth="August",
                    byear="1976"))
    else:
        contact = contacts_not_in_group[randrange(len(contacts_not_in_group))]
    app.contact.add_contacts_to_group(groups_list[index].group_id, [contact])
    assert len(
        list(filter(lambda x: x.contact_id == contact.contact_id, orm.get_contacts_in_group(groups_list[index])))) != 0
    assert len(list(
        filter(lambda x: x.contact_id == contact.contact_id, orm.get_contacts_not_in_group(groups_list[index])))) == 0


def test_delete_contact_from_group(app, orm):
    groups_list = orm.get_group_list()
    if len(groups_list) == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
        groups_list = orm.get_group_list()
    index = randrange(len(groups_list))
    contacts_in_group = orm.get_contacts_in_group(groups_list[index])
    if len(contacts_in_group) == 0:
        if len(orm.get_contacts_not_in_group(groups_list[index])) == 0:
            app.contact.create(
                Contact(firstname="Ivan", lastname="Petrov", nickname="pivan", title="developer", company="DevCompany",
                        address="Moscow", mobilephone="+7 933 933 4545", email="petrov@mail.ru", bday="5", bmonth="August",
                        byear="1976"))
        contacts_not_in_group = orm.get_contacts_not_in_group(groups_list[index])
        contact = contacts_not_in_group[randrange(len(contacts_not_in_group))]
        app.contact.add_contacts_to_group(groups_list[index].group_id, [contact])
    else:
        contact = contacts_in_group[randrange(len(contacts_in_group))]
    app.contact.delete_contacts_from_group(groups_list[index].group_id, [contact])
    assert len(
        list(filter(lambda x: x.contact_id == contact.contact_id, orm.get_contacts_in_group(groups_list[index])))) == 0
    assert len(list(
        filter(lambda x: x.contact_id == contact.contact_id, orm.get_contacts_not_in_group(groups_list[index])))) != 0
