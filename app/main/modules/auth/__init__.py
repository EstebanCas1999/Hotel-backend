import configparser
import os

from app import public_api
from app.main.modules.auth.resource import AuthResource


def init_app(app, **kwargs):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'), encoding="utf-8-sig")
    app.config['AUTH'] = config
    public_api.add_resource(AuthResource, '/auth')
