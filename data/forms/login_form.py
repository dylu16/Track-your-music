from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class LoginForm(FlaskForm):
    email = StringField(' Email ', render_kw={"placeholder": " Enter your Email "})
    password = PasswordField(' Password ', render_kw={"placeholder": " Enter the Password "})
    submit = SubmitField(' Login ')
