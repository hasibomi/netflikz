from flask import Blueprint

from .auth.views import ViewSignUp, ViewLogin, ViewLogOut


api = Blueprint("api", __name__, url_prefix="/api")

# Routing starts from here.

api.add_url_rule("/signup/", view_func=ViewSignUp.as_view("signup"))
api.add_url_rule("/signin/", view_func=ViewLogin.as_view("login"))
api.add_url_rule("/signout/", view_func=ViewLogOut.as_view("logout"))
