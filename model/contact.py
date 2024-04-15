import re
from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 all_phones_from_home_page=None, homephone=None, mobilephone=None, workphone=None, email=None,
                 email2=None, email3=None, all_emails_from_home_page = None, bday=None, bmonth=None, byear=None,
                 contact_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.contact_id = contact_id

    def __repr__(self):
        return "%s:%s:%s" % (self.contact_id, self.firstname, self.lastname)

    def __eq__(self, other):
        return ((self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id)
                and self.firstname == other.firstname and self.lastname == other.lastname)

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None and x != "",
                               [contact.email.strip(), contact.email2.strip(), contact.email3.strip()]))
