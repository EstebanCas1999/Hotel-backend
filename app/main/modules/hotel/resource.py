from flask_restful import Resource
from .schemas import HotelPaginationSchema
from .service import HotelService

hotel_pagination_schema = HotelPaginationSchema()


class HotelResource(Resource):
    @classmethod
    def get(cls):
        data = HotelService.get_hotel_list()
        return hotel_pagination_schema.dump(data)