from flask import request
from flask_restful import Resource
from .schemas import RoomPaginationSchema, FindRoomsSchema
from .service import RoomService

room_pagination_schema = RoomPaginationSchema()
find_rooms_schema = FindRoomsSchema()


class RoomResource(Resource):
    @classmethod
    def get(cls):
        find_rooms_schema_data = find_rooms_schema.load(request.get_json())
        data = RoomService.get_room_list_by_hotel(find_rooms_schema_data)
        return room_pagination_schema.dump(data)
