from flask import request
from flask.views import View


class ViewLogin(View):
    methods = ["GET"]

    def dispatch_request(self):
        return {
            "status": "success",
            "result": "Login Page"
        }
