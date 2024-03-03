from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New group", header="New group header", footer="New group footer"))
    app.session.logout()