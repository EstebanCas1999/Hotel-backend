from marshmallow import fields, Schema


class HotelFilterSchema(Schema):
    id = fields.Integer(required=True,data_key='id', attribute='id')
    name = fields.String(required=True, data_key='name', attribute='name')
    stairs = fields.Float(required=True, data_key='stairs', attribute='stairs')
    city = fields.String(required=True, data_key='city', attribute='city')
    image = fields.String(required=True, data_key='image', attribute='image')


class HotelPaginationSchema(Schema):
    results = fields.List(fields.Nested(HotelFilterSchema), required=True, attribute='results')