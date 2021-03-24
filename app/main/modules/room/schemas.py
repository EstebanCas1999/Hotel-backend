from marshmallow import fields, Schema


class RoomTypeSchema(Schema):
    code = fields.String(required=True, data_key='code', attribute='code')
    description = fields.String(required=True, data_key='description', attribute='description')


class FindRoomsSchema(Schema):
    hotel_id = fields.Integer(required=True, data_key='hotel_id', attribute='hotel_id')


class RoomFilterSchema(Schema):
    hotel_image = fields.String(required=True, data_key='hotel_image', attribute='hotel_image')
    hotel_name = fields.String(required=True, data_key='hotel_name', attribute='hotel_name')
    hotel_stairs = fields.Float(required=True, data_key='hotel_stairs', attribute='hotel_stairs')
    room_type = fields.Nested(RoomTypeSchema(), data_key='room_type')
    room_price = fields.String(required=True, data_key='room_price', attribute='room_price')
    room_image_first = fields.String(required=True, data_key='room_image_first', attribute='room_image_first')
    room_image_second = fields.String(required=True, data_key='room_image_second', attribute='room_image_second')
    room_image_third = fields.String(required=True, data_key='room_image_third', attribute='room_image_third')


class RoomPaginationSchema(Schema):
    results = fields.List(fields.Nested(RoomFilterSchema), required=True, attribute='results')
