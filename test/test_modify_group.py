from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group", header="New group header", footer="New group footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New group header 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
