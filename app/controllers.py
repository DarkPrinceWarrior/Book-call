
from app.models.db_setup import db_session
from app.models.entities import Role, Users


def selectAll():
    users = db_session.query(Users).all()
    for user in users:
        print("login: ", user.login,'\nemail: ', user.email)
        print("----------------")
