import abc
from src import db


class Repository(type=abc.ABCMeta):
    _model: db.Model = None

    @classmethod
    def get_by_id(cls, id_):
        return cls._model.query.filter_by(id=id_).first()
