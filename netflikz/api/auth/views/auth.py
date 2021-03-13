from flask import request
from flask.views import View
from netflikz.api.auth.forms import FormSignUp


class ViewSignUp(View):
    methods = ["POST"]

    def dispatch_request(self):
        form = FormSignUp.from_json(request.json)

        if form.validate():
            return {
                "status": "success",
                "result": {
                    "email": form.email.data,
                    "password": form.password.data
                }
            }

        return {
            "status": "error",
            "result": form.errors
        }


class ViewLogin(View):
    methods = ["GET"]

    def dispatch_request(self):
        return {
            "status": "success",
            "result": "Login Page"
        }
