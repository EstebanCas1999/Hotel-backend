from marshmallow import fields, Schema


class RoleSchema(Schema):
    code = fields.String(required=True, data_key='code', attribute='code')
    description = fields.String(required=True, data_key='description', attribute='description')


class CreateUserSchema(Schema):
    name = fields.String(required=True, data_key='name')
    surnames = fields.String(required=True, data_key='surnames')
    role = fields.String(required=True, data_key='role')
    password = fields.String(required=True, data_key='password')
    document_number = fields.String(required=True, data_key='documentNumber')
