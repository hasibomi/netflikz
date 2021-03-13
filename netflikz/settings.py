import os
import wtforms_json

from flask import Flask
from flask_migrate import Migrate

from .database import db
from .views import Home
from .api import api


def create_app(test_config=None):
    """Create the instance of the application."""

    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if test_config is None:
        app.config.from_pyfile('config.py', silent=False)
    else:
        app.config.from_mapping(test_config)

    # Instantiate the Database.
    db.init_app(app=app)
    migrate = Migrate(app=app, db=db)

    # Initialize WTForms to handle JSON data.
    wtforms_json.init()

    # Routing starts from here.
    app.add_url_rule("/", view_func=Home.as_view("home"))
    app.register_blueprint(api)

    return app
