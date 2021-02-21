from werkzeug.security import generate_password_hash

from app.main.modules.shared.generic_utils import GenericService, transaction
from app.main.modules.user.model import User
from app.main.modules.user.schemas import CreateUserSchema
from app.main.modules.shared.exceptions import ConflictException
from flask import current_app as app


class UserService(GenericService):

    @classmethod
    @transaction
    def create_user(cls, create_user_schema: CreateUserSchema):
        document_number = create_user_schema.get('document_number', '')
        exist_user = User.exist_user(document_number=document_number)
        if exist_user is None:
            user = User()
            user.document_number = document_number
            user.role = create_user_schema.get('role', '')
            user.name = create_user_schema.get('name', '')
            user.surnames = create_user_schema.get('surnames')
            user.password = generate_password_hash(create_user_schema.get('password', ''), method='sha256')
            cls.save(user)
        else:
            user_message = dict(app.config.get('USER', {})).get('MESSAGE', {})
            raise ConflictException(user_message.get('DUPLICATE_USER_BY_DOCUMENT_NUMBER', ''))
