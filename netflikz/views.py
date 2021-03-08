from flask.views import View
from flask import render_template


class Home(View):
    methods = ["GET"]

    def dispatch_request(self):
        return render_template("index.html")
