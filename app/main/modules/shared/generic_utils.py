import functools

from app.main.extensions import db


class GenericService:

    @classmethod
    def save(cls, entity):
        db.session.begin(subtransactions=True)
        db.session.add(entity)
        db.session.commit()

    @classmethod
    def update(cls):
        db.session.commit()

    @classmethod
    def delete(cls, entity):
        db.session.delete(entity)
        db.session.commit()


def transaction(f):
    @functools.wraps(f)
    def function_that_runs_f(*args, **kwargs):
        try:
            f(*args, **kwargs)
            db.session.commit()
        except () as err:
            raise err
        except Exception as err:
            db.session.rollback()
            raise err

    return function_that_runs_f
