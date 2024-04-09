from pony.orm import *


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')

    def __init__(self, host="127.0.0.1", name="addressbook", user="root", password=""):
        self.db.bind("mysql", host=host, database=name, user=user, password=password)
        self.db.generate_mapping()

    @db_session
    def get_group_list(self):
        return list(select(g for g in ORMFixture.ORMGroup))
