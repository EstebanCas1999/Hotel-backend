from marshmallow import fields, Schema


class ProfileSchema(Schema):
    code = fields.String(required=True, data_key='code', attribute='code')
    description = fields.String(required=True, data_key='description', attribute='description')


class LoginRequestSchema(Schema):
    document_number = fields.String(required=True, data_key='documentNumber', attribute='documentNumber')
    password = fields.String(required=True, data_key='password', attribute='password')


class LoginResponseSchema(Schema):
    id = fields.Integer(data_key='id')
    username = fields.String(data_key='username')
    profile = fields.Nested(ProfileSchema(), data_key='profile')
