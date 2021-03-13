from flask import request
from flask.views import View
from werkzeug.security import generate_password_hash, check_password_hash

from netflikz.database import db
from netflikz.api.auth.forms import FormSignUp
from netflikz.api.auth.models import User


class ViewSignUp(View):
    methods = ["POST"]

    def dispatch_request(self):
        form = FormSignUp.from_json(request.json)

        if not form.validate():
            return {
                "status": "error",
                "result": form.errors
            }

        user = User(
            email=form.email.data,
            password=generate_password_hash(form.password.data, method="sha256"),
        )

        db.session.add(user)
        db.session.commit()

        return {
            "status": "success"
        }


class ViewLogin(View):
    methods = ["GET"]

    def dispatch_request(self):
        return {
            "status": "success",
            "result": "Login Page"
        }
