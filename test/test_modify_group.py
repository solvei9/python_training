from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
    app.group.modify_first_group(Group(name="New group", header="New group header", footer="New group footer"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
    app.group.modify_first_group(Group(name="New group 1"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group("Group 2", "Group 2 header", "Group 2 footer"))
    app.group.modify_first_group(Group(header="New group header 1"))
