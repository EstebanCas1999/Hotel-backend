from http import HTTPStatus

from flask_jwt_extended import JWTManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.main.log_setup import LogSetup

db = SQLAlchemy(session_options={'autocommit': False})
migrate = Migrate(compare_type=True)
logging = LogSetup()
jwt = JWTManager()


def init_app(app: Flask) -> None:
    for extension in (db, logging, jwt):
        extension.init_app(app)
    migrate.init_app(app, db)
