from flask import Flask

from .config import config_by_name
from . import extensions
from . import modules


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    extensions.init_app(app)
    modules.init_app(app)

    return app
