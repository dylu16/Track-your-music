from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', render_kw={"placeholder": " Enter Email "})
    submit = SubmitField('Submit')
