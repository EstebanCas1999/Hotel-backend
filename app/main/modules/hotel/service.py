from app.main.modules.hotel.model import Hotel
from app.main.modules.shared.generic_utils import GenericService


class HotelService(GenericService):
    @classmethod
    def get_hotel_list(cls):
        list_hotel = Hotel.find_all_hotels()
        dict_hotels_response = dict(
            results=[]
        )
        list_hotel_data = []
        for hotel in list_hotel:
            list_hotel_data.append(dict(
                id=hotel.id,
                name=hotel.name,
                stairs=hotel.stairs,
                city=hotel.city_name
            ))
        dict_hotels_response.update(dict(results=list_hotel_data))
        return dict_hotels_response
