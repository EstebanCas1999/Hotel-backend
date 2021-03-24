from collections import namedtuple
from enum import Enum

Role = namedtuple('Role', ['code', 'description'])


class RoleEnum(Enum):
    ADMIN = Role('AD', 'Administrador')
    CLIENT = Role('CL', 'Cliente')
    WORKER = Role('WR', 'Empleado')

    @property
    def get_code(self):
        return self.value.code

    @property
    def get_description(self):
        return self.value.description
