from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField


class UploadFileForm(FlaskForm):
    upload_file = FileField('Upload file')
    submit = SubmitField('Upload')
