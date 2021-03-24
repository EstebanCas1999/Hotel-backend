from flask import request
from flask_restful import Resource
from .schemas import LoginRequestSchema, LoginResponseSchema
from .service import AuthService

login_request_schema = LoginRequestSchema()
login_response_schema = LoginResponseSchema()


class AuthResource(Resource):

    @classmethod
    def post(cls):
        login_schema_data = login_request_schema.load(request.get_json(), unknown='EXCLUDE')
        auth_user = AuthService.validate_login(login_schema_data)
        return login_response_schema.dump(auth_user)
