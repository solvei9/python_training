import random

from pytest_bdd import given, when, then, parsers
from model.contact import Contact


@given('a contact list', target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()


@given(parsers.parse('a contact with {firstname}, {lastname}, {nickname}, {address}, {mobilephone}, {email}'),
       target_fixture='new_contact')
def new_contact(firstname, lastname, nickname, address, mobilephone, email):
    return Contact(firstname=firstname, lastname=lastname, nickname=nickname, address=address, mobilephone=mobilephone,
                   email=email)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old contact with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list', target_fixture='non_empty_contact_list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='firstname2', lastname='lastname2'))
    return db.get_contact_list()


@given('a random contact from the list', target_fixture='random_contact')
def random_contact_from_the_list(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.contact_id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@when(parsers.parse('I set {firstname}, {lastname}, {nickname} for the contact'), target_fixture='modified_contact')
def modify_contact(app, random_contact, firstname, lastname, nickname):
    modified_contact = (
        Contact(firstname=firstname, lastname=lastname, nickname=nickname, contact_id=random_contact.contact_id))
    app.contact.modify_contact_by_id(random_contact.contact_id, modified_contact)
    return modified_contact


@then('the new contact list is equal to the old contact with the modified contact')
def verify_contact_modified(db, non_empty_contact_list, random_contact, modified_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    old_contacts.append(modified_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
