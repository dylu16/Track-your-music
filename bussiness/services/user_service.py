from bussiness.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.__user_repository = UserRepository()

    def add(self, _firstname, _lastname, _email, _password, _is_admin=False):
        return self.__user_repository.add(_firstname, _lastname, _email, _password, _is_admin)

    def get_by_email(self, _email):
        return self.__user_repository.get_by_email(_email)

    def update_password(self, _user, _password):
        return self.__user_repository.update_password(_user, _password)
