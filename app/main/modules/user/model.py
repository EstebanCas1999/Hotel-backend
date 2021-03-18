from sqlalchemy.orm.exc import NoResultFound

from app.main.extensions import db
from app.main.modules.shared.enums.role_enum import RoleEnum


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=20), index=False, unique=False, nullable=False)
    surnames = db.Column(db.String(length=20), index=False, unique=False, nullable=False)
    role = db.Column(db.Enum(RoleEnum), index=False, unique=False, nullable=False)
    document_number = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(length=255), index=False, unique=False, nullable=False)

    @classmethod
    def exist_user(cls, document_number):
        try:
            return db.session.query(User).filter_by(document_number=document_number).one()
        except NoResultFound:
            return None
