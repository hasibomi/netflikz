from flask import request
from flask.views import View

from netflikz.api.auth.models import User as UserModel
from netflikz.libs import JWT


class ViewProtected:
    def __init__(self):
        token = None
        header = request.headers.get("Authorization")
        request.user = None

        if header:
            token = header.split(" ")[1]

        if token is None:
            pass

        decoded_token = JWT.decode(token=token)
        user = UserModel.query.get(decoded_token)

        if user:
            self.user = user
