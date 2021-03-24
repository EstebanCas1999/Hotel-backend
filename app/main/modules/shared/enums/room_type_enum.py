from collections import namedtuple
from enum import Enum

RoomType = namedtuple('room_type', ['code', 'description'])


class RoomTypeEnum(Enum):
    SIMPLE = RoomType('SMP', 'Sencilla')
    DOUBLE = RoomType('DBL', 'Doble')

    @property
    def get_code(self):
        return self.value.code

    @property
    def get_description(self):
        return self.value.description
