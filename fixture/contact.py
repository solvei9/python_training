import re
from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        # submit contact
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.app.contact.return_to_contacts_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.app.contact.return_to_contacts_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contact)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.app.contact.return_to_contacts_page()
        self.contact_cache = None

    def open_first_contact_to_edit(self):
        self.open_contact_to_edit_by_index(0)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "a[href='edit.php?id=%s']" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.XPATH, "//img[@alt='Details']")[index].click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email)
        self.select_field_value("bday", contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

    def select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.XPATH, "//option[@value='" + text + "']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_elements(By.NAME, "selected[]")[index].click()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.app.contact.return_to_contacts_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.app.contact.return_to_contacts_page()
        self.contact_cache = None

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "tr[name=entry]"):
                properties = element.find_elements(By.CSS_SELECTOR, "td")
                contact_id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                address = properties[3].text
                all_emails = properties[4].text
                all_phones = properties[5].text
                self.contact_cache.append(
                    Contact(firstname=properties[2].text, lastname=properties[1].text, contact_id=contact_id,
                            address=address, all_emails_from_home_page=all_emails,
                            all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        contact_id = wd.find_element(By.NAME, "id").get_attribute("value")
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(contact_id=contact_id, firstname=firstname, lastname=lastname, address=address,
                       homephone=homephone,
                       workphone=workphone, mobilephone=mobilephone, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone)
