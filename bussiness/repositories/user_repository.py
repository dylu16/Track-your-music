from presentation.server import db
from data.models.user import User


class UserRepository:
    def __init__(self):
        self.__db_context = db.session

    def add(self, _firstname, _lastname, _email, _password, _is_admin):
        user = User(
            firstname=_firstname,
            lastname=_lastname,
            email=_email,
            password=_password,
            is_admin=_is_admin
        )
        self.__db_context.add(user)
        self.__db_context.commit()

    def get_by_email(self, _email):
        return self.__db_context.query(User).filter(User.email == _email).first()

    def update_password(self, _user, _password):
        try:
            _user.password = _password
            self.__db_context.commit()
        except Exception as e:
            print("Exception occurred on user update password: {}".format(e))
