from flask import Flask

from .views import Home
from .auth import auth


def create_app(test_config=None):
    """Create the instance of the application."""

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Routing starts from here.
    app.add_url_rule("/", view_func=Home.as_view("home"))
    app.register_blueprint(auth)

    return app
