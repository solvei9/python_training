from model.group import Group


def test_modify_group(app):
    app.group.modify_first_group(Group(name="New group", header="New group header", footer="New group footer"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group 1"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New group header 1"))
