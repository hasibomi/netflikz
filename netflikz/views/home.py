from flask.views import View


class Home(View):
    methods = ["GET"]

    def dispatch_request(self):
        return {
            "status": "success",
            "result": "ok"
        }
