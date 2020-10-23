from bussiness.repositories.pending_account_repository import PendingAccountRepository


class PendingAccountService:
    def __init__(self):
        self.__pending_account_repository = PendingAccountRepository()

    def add(self, _firstname, _lastname, _email, _password, _token, _is_admin=False):
        return self.__pending_account_repository.add(_firstname, _lastname, _email, _password, _token, _is_admin)

    def get_by_token(self, _token):
        return self.__pending_account_repository.get_by_token(_token)

    def delete_by_id(self, _id):
        return self.__pending_account_repository.delete_by_id(_id)
