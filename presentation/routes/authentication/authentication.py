from bussiness.services.user_service import UserService
from bussiness.services.pending_account_service import PendingAccountService
from data.utils.validator_user import ValidatorUser
from data.utils.email import send_confirmation_email
from data.utils.email import send_password_email
from data.utils.random import get_random_password
from data.forms.forgot_password_form import ForgotPasswordForm
from data.forms.registration_form import RegistrationForm
from data.forms.login_form import LoginForm
from presentation.server import bcrypt
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user

auth_bp = Blueprint('auth_bp', __name__)

user_service = UserService()
pending_account_service = PendingAccountService()


@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.submit.data:
        lastname = form.lastname.data.strip().title()
        firstname = form.firstname.data.strip().title()
        email = form.email.data.strip().lower()
        password = form.password.data
        confirm_password = form.confirm_password.data

        validator_user = ValidatorUser(
            lastname,
            firstname,
            email,
            password,
            confirm_password
        )
        result_validate_user = validator_user.validate()

        if isinstance(result_validate_user, tuple):
            flash(result_validate_user[1], 'danger')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            token = send_confirmation_email(
                email,
                lastname,
                firstname
            )
            pending_account_service.add(
                _lastname=lastname,
                _firstname=firstname,
                _email=email,
                _password=hashed_password,
                _token=token
            )
            flash(f"Un email de confirmare a fost trimis la " + email + "!", 'success')

            return redirect(url_for('auth_bp.login'))

    return render_template("authentication/register.html", form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.submit.data:
        email = form.email.data.strip().lower()
        password = form.password.data

        if not email or not password:
            flash('Campurile nu au voie sa fie goale!', 'danger')
            return redirect(url_for('auth_bp.login'))

        user = user_service.get_by_email(email)

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for('app_bp.application'))
        else:
            flash('Logarea nu a reusit, verifica din nou email-ul si parola', 'danger')

    return render_template("authentication/login.html", form=form)


@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = user_service.get_by_email(form.email.data.lower())
        random_password = get_random_password()
        if not user:
            flash('Email-ul {} nu exista in baza de date! '.format(form.email.data.lower()), 'danger')
        elif user:
            user_service.update_password(user, bcrypt.generate_password_hash(random_password).decode('utf-8'))
            send_password_email(form.email.data.lower(), random_password)
            flash('Un email cu noua parola a fost trimis catre {}! '.format(form.email.data.lower()), 'success')

    return render_template("authentication/forgot_password.html", form=form)


@auth_bp.route('/confirm_email/<token>')
def confirm_email(token):
    pending_account = pending_account_service.get_by_token(token)

    if not pending_account:
        flash(f"Token-ul a expirat, inregistrati-va din nou!", 'danger')
        return redirect(url_for('auth_bp.register'))

    user_service.add(
        _lastname = pending_account.lastname,
        _firstname = pending_account.firstname,
        _email = pending_account.email,
        _password = pending_account.password
    )

    pending_account_service.delete_by_id(pending_account.id)

    flash(f"Ai confirmat emailul cu succes, acum te poti conecta!", 'success')
    return redirect(url_for('auth_bp.login'))


@auth_bp.route('/app/logout/')
def logout():
    logout_user()
    flash(f"Te-ai delogat cu succes!", "success")
    return redirect(url_for('auth_bp.login'))
