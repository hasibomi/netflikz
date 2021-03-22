from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

from netflikz.database import db
from netflikz.libs import JWT
from netflikz.libs.models import BlacklistedToken
from netflikz.api.auth.models import User as UserModel
from .exceptions import AuthMixinException


class AuthMixin(object):
    def create(self, **data) -> UserModel:
        data["password"] = generate_password_hash(data["password"], method="sha256")
        user = UserModel(**data)

        db.session.add(user)
        db.session.commit()

        return user

    def __validate_credentials(self, email, password) -> UserModel:
        user = UserModel.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            raise AuthMixinException("Invalid credentials")

        return user

    def login(self, email, password):
        user = self.__validate_credentials(email=email, password=password)

        return JWT.encode(user_id=user.id, data={
            "email": user.email
        })

    def logout(self, token) -> None:
        blacklist_token = BlacklistedToken(token=token)

        try:
            db.session.add(blacklist_token)
            db.session.commit()
        except:
            pass


_authmixinobj = AuthMixin()
create = _authmixinobj.create
login = _authmixinobj.login
logout = _authmixinobj.logout
