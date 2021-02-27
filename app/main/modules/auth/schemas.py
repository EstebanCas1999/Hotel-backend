from marshmallow import fields, Schema


class LoginSchema(Schema):
    document_number = fields.String(required=True, data_key='documentNumber', attribute='documentNumber')
    password = fields.String(required=True, data_key='password', attribute='password')
