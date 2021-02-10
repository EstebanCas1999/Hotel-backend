from http import HTTPStatus

from flask_jwt_extended import JWTManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(session_options={'autocommit': False})
migrate = Migrate()
jwt = JWTManager()


def init_app(app: Flask) -> None:
    for extension in (db, jwt):
        extension.init_app(app)
    migrate.init_app(app, db)
