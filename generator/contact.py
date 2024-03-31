import jsonpickle
import os.path
import getopt
import sys
import random
import model.general
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

f = "data/contacts.json"

for o, a in opts:
    if o == "-f":
        f = a

testdata = [
    Contact(firstname=firstname, lastname=lastname, nickname=model.general.random_string("", 9),
                title="developer", company="DevCompany", address="Moscow",
                homephone=model.general.random_phone(), mobilephone=mobilephone, workphone=model.general.random_phone(),
                email=email, email2=model.general.random_email(), email3=model.general.random_email(),
                bday="5", bmonth="August", byear=random.randrange(1900, 2025))
    for firstname in ["", model.general.random_string("Ivan", 5)]
    for lastname in ["", model.general.random_string("Petrov", 3)]
    for mobilephone in ["", model.general.random_phone()]
    for email in ["", model.general.random_email()]
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
