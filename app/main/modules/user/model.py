from app.main.extensions import db
from app.main.modules.shared.enums.role_enum import RoleEnum


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=20), index=False, unique=False, nullable=False)
    surnames = db.Column(db.String(length=20), index=False, unique=False, nullable=False)
    role = db.Column(db.Enum(RoleEnum), index=False, unique=False, nullable=False)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(length=255), index=False, unique=False, nullable=False)
