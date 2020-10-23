from flask import url_for
from itsdangerous import URLSafeTimedSerializer
from presentation.server import mail, Message

serializer = URLSafeTimedSerializer('Thisisasecret!')

def send_confirmation_email(recipientEmail, lastname, firstname):
    token = serializer.dumps(recipientEmail, salt='email-confirm')
    msg = Message('[Confirmare email] Track your music', sender='trackyourmusic16@gmail.com', recipients=[recipientEmail])

    link = url_for('auth_bp.confirm_email', token=token, _external=True)

    msg.body = 'Multumim pentru inregistrare {} {} acest email a fost trimis cu scopul de a vedea daca adresa ' \
               'inregistrarii este una reala \n' \
               'Linkul tau de confirmare este: {}'.format(lastname,firstname,link)

    mail.send(msg)
    return token

def send_password_email(recipientEmail, password):
    token = serializer.dumps(recipientEmail, salt='forgot-password')
    msg = Message('[Uitare parola] Track your music', sender='trackyourmusic16@gmail.com', recipients=[recipientEmail])

    msg.body = 'Acest email a fost trimis la cererea dumneavoastra cu privire la uitarea parolei \n' \
               'Noua parola este: {}'.format(password)

    mail.send(msg)
    return token
