from werkzeug.security import check_password_hash

from app.main import ObjectNotFoundException
from app.main.modules.auth.schemas import LoginRequestSchema
from app.main.modules.shared.generic_utils import GenericService
from app.main.modules.user.model import User
from flask import current_app as app


class AuthService(GenericService):
    @classmethod
    def validate_login(cls, login_schema_data: LoginRequestSchema):
        user_find_by_document = User.exist_user(document_number=login_schema_data.get('documentNumber', ''))
        auth_message = dict(app.config.get('AUTH', {})).get('MESSAGE', {})
        if user_find_by_document:
            user = user_find_by_document
            if user and check_password_hash(user.password, login_schema_data.get('password', '')):
                login_dict_response = dict(username=user.name, id=user.id, profile=dict(code=user.role.get_code,
                                                                                        description=user.role.
                                                                                        get_description))
                return login_dict_response
            else:
                raise ObjectNotFoundException(auth_message.get('MESSAGE_RESPONSE', ''))
        else:
            raise ObjectNotFoundException(auth_message.get('MESSAGE_RESPONSE', ''))
