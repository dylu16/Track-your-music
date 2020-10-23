from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField


class UploadSongForm(FlaskForm):
    upload_song = FileField('Upload song')
    submit_button = SubmitField('Add song')
