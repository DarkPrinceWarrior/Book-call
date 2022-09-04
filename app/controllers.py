from app.models.db_setup import db_session
from app.models.entities import Role, Users


def register_user(dict_user):
    newUser = Users(login=dict_user["login"],
                    email=dict_user["email"],
                    password=dict_user["password"],
                    role_id=2)
    db_session.add(newUser)
    db_session.commit()


def login_user(login, password):
    try:
        db_session.query(Users).filter_by(login=login, password=password).one()
        return True
    except:
        return False


def selectAll():
    users = db_session.query(Users).all()
    for user in users:
        print("login: ", user.login, '\nemail: ', user.email)
        print("----------------")
