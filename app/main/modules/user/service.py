from werkzeug.security import generate_password_hash

from app.main.modules.shared.generic_utils import GenericService, transaction
from app.main.modules.user.model import User
from app.main.modules.user.schemas import CreateUserSchema


class UserService(GenericService):

    @classmethod
    @transaction
    def create_user(cls, create_user_schema: CreateUserSchema):
        user = User()
        user.username = create_user_schema.get('username', '')
        user.role = create_user_schema.get('role', '')
        user.name = create_user_schema.get('name', '')
        user.surnames = create_user_schema.get('surnames')
        user.password = generate_password_hash(create_user_schema.get('password', ''), method='sha256')
        cls.save(user)
