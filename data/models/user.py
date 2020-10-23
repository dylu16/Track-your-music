from presentation.server import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def data_as_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "role": self.is_admin,
            "img_path": self.img_path
        }

    def __repr__(self):
        return "User(\n" \
               "\tID: " + str(self.id) + "\n" \
               "\tFirstname: " + self.firstname + "\n" \
               "\tLastname: " + self.lastname + "\n" \
               "\tEmail: " + self.email + "\n" \
               "\tIs admin: " + str(self.is_admin) + "\n" \
               "\tImg path: " + self.img_path + "\n" \
               ")"
