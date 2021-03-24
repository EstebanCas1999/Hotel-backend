from app.main import db
from app.main.modules.administration.model import City


class Hotel(db.Model):
    __tablename__ = "hotels"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=80), index=False, unique=False, nullable=False)
    stairs = db.Column(db.Float, index=False, unique=False, nullable=False)
    city_id = db.Column(db.BigInteger, db.ForeignKey('cities.id', name='FK_city_hotel_id'))
    image_hotel = db.Column(db.TEXT(10000), index=False, unique=False, nullable=False)

    @classmethod
    def find_all_hotels(cls):
        return db.session.query(Hotel.id, Hotel.name, Hotel.stairs, City.name.label('city_name')). \
            join(Hotel, (Hotel.city_id == City.id)).all()
