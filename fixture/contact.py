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
        self.open_edit_form_for_contact(index)
        self.fill_contact_form(contact)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.app.contact.return_to_contacts_page()
        self.contact_cache = None

    def open_edit_form_for_first_contact(self):
        self.open_edit_form_for_contact(0)

    def open_edit_form_for_contact(self, index):
        wd = self.app.wd
        # open modification form for first contact
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
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
                self.contact_cache.append(Contact(lastname=properties[1].text, firstname=properties[2].text, contact_id=contact_id))
        return list(self.contact_cache)
