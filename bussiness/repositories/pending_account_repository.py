from presentation.server import db
from data.models.pending_account import PendingAccount


class PendingAccountRepository:
    def __init__(self):
        self.__db_context = db.session

    def add(self, _firstname, _lastname, _email, _password, _token, _is_admin):
        pending_account = PendingAccount(
            firstname=_firstname,
            lastname=_lastname,
            email=_email,
            password=_password,
            is_admin=_is_admin,
            token=_token
        )
        self.__db_context.add(pending_account)
        self.__db_context.commit()

    def get_by_token(self, _token):
        return self.__db_context.query(PendingAccount).filter(PendingAccount.token == _token).first()

    def delete_by_id(self, _id):
        try:
            self.__db_context.query(PendingAccount).filter(PendingAccount.id == _id).delete()
            self.__db_context.commit()
            return True
        except Exception as e:
            print("Exception pending_account_repository.delete_by_id(): {}".format(e))
            return False

