import random
import model.general
from model.contact import Contact


testdata = [
    Contact(firstname="firstname1", lastname="lastname1", nickname=model.general.random_string("", 9),
                title="developer", company="DevCompany", address="Moscow",
                homephone=model.general.random_phone(), mobilephone="+7 911 911 1212", workphone=model.general.random_phone(),
                email="email1@email1.tu", email2=model.general.random_email(), email3=model.general.random_email(),
                bday="5", bmonth="August", byear=random.randrange(1900, 2025)),
    Contact(firstname="firstname2", lastname="lastname2", nickname=model.general.random_string("", 9),
                title="developer", company="DevCompany", address="Moscow",
                homephone=model.general.random_phone(), mobilephone="+7 922 922 1212", workphone=model.general.random_phone(),
                email="email2@email2.tu", email2=model.general.random_email(), email3=model.general.random_email(),
                bday="5", bmonth="August", byear=random.randrange(1900, 2025))
]
