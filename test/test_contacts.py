from random import randrange
from model.contact import merge_phones_like_on_home_page
from model.contact import merge_emails_like_on_home_page


def test_some_contact_on_home_page(app):
    # select random contact on home page
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = contact_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
