from model.group import Group
from random import randrange


def test_modify_group(app, db, check_ui):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
        old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group", header="New group header", footer="New group footer")
    group.group_id = old_groups[index].group_id
    app.group.modify_group_by_id(group.group_id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.modify_group_by_index(index, Group(name="New group 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.modify_group_by_index(index, Group(header="New group header 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
