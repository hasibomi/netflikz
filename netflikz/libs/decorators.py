from flask import request

from .jwt import JWT
from netflikz.api.auth.models import User as UserModel


def view_protected(function):
    def wrapper(args):
        """
        :param
            args: Default arguments that are being passed by Flask
        """

        token = None
        header = request.headers.get("Authorization")

        if header:
            token = header.split(" ")[1]

        if token is None:
            return {
                "status": "error",
                "result": "Token is missing"
            }

        if JWT.is_blacklisted(token=token):
            return {
                "status": "error",
                "result": "The token has been blacklisted"
            }

        try:
            decoded_token = JWT.decode(token=token)
            user = UserModel.query.get(decoded_token)

            if user:
                args.user = user
                args.token = token

            return function(args)
        except Exception as e:
            return {
                "status": "error",
                "result": str(e)
            }

    return wrapper
