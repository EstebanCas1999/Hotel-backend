import configparser
import os

from app import api
from app.main.modules.room.resource import RoomResource


def init_app(app, **kwargs):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'), encoding="utf-8-sig")
    app.config['ROOM'] = config
    api.add_resource(RoomResource, '/room')
