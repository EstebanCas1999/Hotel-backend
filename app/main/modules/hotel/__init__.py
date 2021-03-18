import configparser
import os

from app import api
from app.main.modules.hotel.resource import HotelResource

def init_app(app, **kwargs):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'), encoding="utf-8-sig")
    app.config['HOTEL'] = config
    api.add_resource(HotelResource, '/hotel')