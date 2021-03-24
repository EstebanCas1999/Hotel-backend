from app.main.modules.room.model import Room
from app.main.modules.room.schemas import FindRoomsSchema
from app.main.modules.shared.generic_utils import GenericService


class RoomService(GenericService):
    @classmethod
    def get_room_list_by_hotel(cls, find_rooms_schema: FindRoomsSchema):
        list_room = Room.room_find_by_hotel_id(find_rooms_schema.get('hotel_id'))
        dict_hotels_response = dict(
            results=[]
        )
        list_room_data = []
        for room in list_room:
            list_room_data.append(dict(
                hotel_image=room.Hotel.image_hotel,
                hotel_name=room.Hotel.name,
                hotel_stairs=room.Hotel.stairs,
                room_type=dict(code=room.Room.room_type.get_code, description=room.Room.room_type.get_description),
                room_price=room.Room.price,
                room_image_first=room.Room.image_room_first,
                room_image_second=room.Room.image_room_second,
                room_image_third=room.Room.image_room_third,
            ))
        dict_hotels_response.update(dict(results=list_room_data))
        return dict_hotels_response
