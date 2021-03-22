from flask import request, jsonify
from flask.views import View

from netflikz.api.auth.forms import FormSignUp, FormSignIn
from netflikz.libs.mixins import auth
from netflikz.libs.decorators import view_protected


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

    @view_protected
    def dispatch_request(self):
        auth.logout(token=self.token)

        return {
            "status": "success"
        }


class ViewProfile(View):
    methods = ["GET"]

    @view_protected
    def dispatch_request(self):
        return {
            "status": "success",
            "result": {
                "email": self.user.email
            }
        }
