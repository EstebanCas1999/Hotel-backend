from app.main import db
from app.main.modules.hotel.model import Hotel
from app.main.modules.shared.enums.room_type_enum import RoomTypeEnum


class Room(db.Model):
    __tablename__ = "rooms"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    price = db.Column(db.String(10), index=False, unique=False, nullable=False)
    room_type = db.Column(db.Enum(RoomTypeEnum), index=False, unique=False, nullable=False)
    hotel_id = db.Column(db.BigInteger, db.ForeignKey('hotels.id', name='FK_room_hotel_id'))
    image_room_first = db.Column(db.TEXT(10000), index=False, unique=False, nullable=False)
    image_room_second = db.Column(db.TEXT(10000), index=False, unique=False, nullable=False)
    image_room_third = db.Column(db.TEXT(10000), index=False, unique=False, nullable=False)

    @classmethod
    def room_find_by_hotel_id(cls, hotel_id):
        return db.session.query(Room, Hotel). \
            join(Room, (Room.hotel_id == Hotel.id)).filter(Hotel.id == hotel_id).all()
