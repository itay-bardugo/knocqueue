import abc
from flask_sqlalchemy.model import Model


class Repository(metaclass=abc.ABCMeta):
    _model: Model = None

    @classmethod
    def get_by_pk(cls, pk):
        return cls._model.query.get(pk)
