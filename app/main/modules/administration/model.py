from app.main.extensions import db


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=80), index=False, unique=True, nullable=False)
    cities = db.relationship('City',
                             foreign_keys='City.department_id',
                             backref=db.backref('department', lazy=True),
                             lazy=True)


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=80), index=False, unique=True, nullable=False)
    department_id = db.Column(db.BigInteger, db.ForeignKey('departments.id', name='FK_department_city_id'))
    hotels = db.relationship('Hotel', foreign_keys='Hotel.city_id', backref=db.backref('hotel', lazy=True),
                            lazy=True)
