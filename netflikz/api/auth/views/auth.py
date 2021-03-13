from flask import request
from flask.views import View
from werkzeug.security import generate_password_hash, check_password_hash

from netflikz.database import db
from netflikz.api.auth.forms import FormSignUp, FormSignIn
from netflikz.api.auth.models import User
from netflikz.libs.models import BlacklistedToken
from netflikz.libs import JWT


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
    methods = ["POST"]

    def dispatch_request(self):
        form = FormSignIn.from_json(request.json)

        if not form.validate():
            return {
                "status": "error",
                "result": form.errors
            }

        user = User.query.filter_by(email=form.email.data).first()

        if not user or not check_password_hash(user.password, form.password.data):
            return {
                "status": "error",
                "result": "Invalid credentials"
            }

        token = JWT.encode(
            user_id=user.id,
            data={
                "email": user.email
            }
        )

        return {
            "status": "success",
            "result": token
        }


class ViewLogOut(View):
    methods = ["POST"]

    def dispatch_request(self):
        token = None
        header = request.headers.get("Authorization")

        if header:
            token = header.split(" ")[1]

        if token is None:
            return {
                "status": "error",
                "message": "Provide a valid token"
            }

        JWT.decode(token=token)

        blacklist_token = BlacklistedToken(token=token)

        try:
            db.session.add(blacklist_token)
            db.session.commit()
        except:
            pass

        return {
            "status": "success"
        }
