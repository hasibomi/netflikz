from flask import request
from flask.views import View

from netflikz.api.auth.forms import FormSignUp, FormSignIn
from netflikz.libs.mixins import auth


class ViewSignUp(View):
    methods = ["POST"]

    def dispatch_request(self):
        form = FormSignUp.from_json(request.json)

        if not form.validate():
            return {
                "status": "error",
                "result": form.errors
            }

        auth.create(email=form.email.data, password=form.password.data)

        return {
            "status": "success"
        }


class ViewLogin(View):
    methods = ["POST"]

    def dispatch_request(self):
        form = FormSignIn.from_json(request.json)

        if not form.validate():
            return {
                "status": "error",
                "result": form.errors
            }

        try:
            token = auth.login(email=form.email.data, password=form.password.data)

            return {
                "status": "success",
                "result": token
            }
        except auth.InvalidCredentialException:
            return {
                "status": "error",
                "result": "Invalid credentials"
            }


class ViewLogOut(View):
    methods = ["POST"]

    def dispatch_request(self):
        auth.logout()

        return {
            "status": "success"
        }
