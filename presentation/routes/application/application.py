from flask import Blueprint, redirect, url_for
from presentation.server import login_manager
app_bp = Blueprint('app_bp', __name__)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


@app_bp.route("/app")
def application():
    return redirect(url_for('recognize_bp.recognize'))
