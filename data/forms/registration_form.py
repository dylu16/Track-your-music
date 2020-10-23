from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegistrationForm(FlaskForm):
    lastname = StringField(' Last Name ', render_kw={"placeholder": " Enter your Last Name "})
    firstname = StringField(' First Name ', render_kw={"placeholder": " Enter your First Name "})
    email = StringField('Email', render_kw={"placeholder": " Enter your Email "})
    password = PasswordField('Passsoword', render_kw={"placeholder": " Enter the Password "})
    confirm_password = PasswordField('Confirm password ', render_kw={"placeholder": " Confirm the Password "})
    submit = SubmitField(' Register ')
