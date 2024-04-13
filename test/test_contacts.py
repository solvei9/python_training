from model.contact import merge_phones_like_on_home_page
from model.contact import merge_emails_like_on_home_page
from model.contact import Contact


def test_all_contact_on_home_page(app, orm, check_ui):
    contact_list = app.contact.get_contact_list()
    for contact_from_home_page in contact_list:
        contact_from_db = orm.get_contact_by_id(contact_from_home_page.contact_id)
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        assert (contact_from_home_page.all_phones_from_home_page ==
                merge_phones_like_on_home_page(
                    Contact(homephone=contact_from_db.homephone, mobilephone=contact_from_db.mobilephone,
                            workphone=contact_from_db.workphone)))
        assert (contact_from_home_page.all_emails_from_home_page ==
                merge_emails_like_on_home_page(
                    Contact(email=contact_from_db.email, email2=contact_from_db.email2, email3=contact_from_db.email3)))
        if check_ui:
            contact_from_edit_page = (
                app.contact.get_contact_info_from_edit_page_by_id(contact_from_home_page.contact_id))
            assert contact_from_home_page.firstname == contact_from_edit_page.firstname
            assert contact_from_home_page.lastname == contact_from_edit_page.lastname
            assert contact_from_home_page.address == contact_from_edit_page.address
            assert (contact_from_home_page.all_phones_from_home_page ==
                    merge_phones_like_on_home_page(contact_from_edit_page))
            assert (contact_from_home_page.all_emails_from_home_page ==
                    merge_emails_like_on_home_page(contact_from_edit_page))
