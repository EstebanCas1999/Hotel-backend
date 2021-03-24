from flask import request
from flask_restful import Resource
from .schemas import CreateUserSchema
from .service import UserService

create_user_schema = CreateUserSchema()


class UserResource(Resource):
    @classmethod
    def post(cls):
        create_user_schema_data = create_user_schema.load(request.get_json())
        UserService.create_user(create_user_schema_data)

