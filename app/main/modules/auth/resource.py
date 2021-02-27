from flask import request
from flask_restful import Resource
from .schemas import LoginSchema
from .service import AuthService

login_schema = LoginSchema()


class AuthResource(Resource):

    @classmethod
    def post(cls):
        login_schema_data = login_schema.load(request.get_json(), unknown='EXCLUDE')
        return AuthService.validate_login(login_schema_data)
