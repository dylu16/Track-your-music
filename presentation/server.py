import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_mail import Mail, Message

presentation_folder_path = os.path.dirname(os.path.abspath(__file__))
config_mail_cfg_path = os.path.join(presentation_folder_path, 'static', 'config_mail.cfg')

template_folder_path = os.path.join(presentation_folder_path, 'templates')

upload_folder_path = os.path.join(presentation_folder_path, 'static', 'uploads')

app = Flask(__name__, template_folder=template_folder_path)

app.config['SECRET_KEY'] = 'arandomstringhardtobebroken'

app.config.from_pyfile(config_mail_cfg_path)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MusicYourTrack16@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = upload_folder_path

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

mail = Mail(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from presentation.routes.home import home_bp
from presentation.routes.authentication.authentication import auth_bp
from presentation.routes.application.application import app_bp
from presentation.routes.application.my_playlist import my_playlist_bp
from presentation.routes.application.edit_playlist import edit_playlist_bp
from presentation.routes.application.recognize import recognize_bp

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(app_bp)
app.register_blueprint(my_playlist_bp)
app.register_blueprint(edit_playlist_bp)
app.register_blueprint(recognize_bp)

from data.models.user import User
from data.models.pending_account import PendingAccount
from data.models.songs import Songs
from data.models.fingerprints import Fingerprints
from data.models.playlist import Playlist
