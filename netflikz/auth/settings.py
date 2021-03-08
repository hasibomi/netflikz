from flask import Blueprint

from .views import ViewLogin


auth = Blueprint('auth', __name__)

auth.add_url_rule("/login/", view_func=ViewLogin.as_view("login"))
