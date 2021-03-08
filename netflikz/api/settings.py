from flask import Blueprint

from .auth.views import ViewLogin


api = Blueprint("api", __name__, url_prefix="/api")

# Routing starts from here.

api.add_url_rule("/login/", view_func=ViewLogin.as_view("login"))
