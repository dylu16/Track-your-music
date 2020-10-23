from presentation.server import db
from data.utils.date import get_datetime_now


class PendingAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    token = db.Column(db.String(100), unique=False, nullable=False)
    register_date = db.Column(db.DateTime, nullable=False, default=get_datetime_now())

    def __init__(self, **kwargs):
        super(PendingAccount, self).__init__(**kwargs)

    @property
    def data_as_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "isAdmin": self.is_admin,
            "register_date": self.register_date
        }

    def __repr__(self):
        return "Pending account(\n" \
               "\tID: " + str(self.id) + "\n" \
               "\tFirstname: " + self.firstname + "\n" \
               "\tLastname: " + self.lastname + "\n" \
               "\tEmail: " + self.email + "\n" \
               "\tIs admin: " + str(self.is_admin) + "\n" \
               "\tRegister date: " + str(self.register_date) + "\n" \
               ")"
