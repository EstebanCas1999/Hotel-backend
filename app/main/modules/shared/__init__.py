import configparser
import os


def init_app(app, **kwargs):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'), encoding="utf-8-sig")
    app.config['COMMON'] = config