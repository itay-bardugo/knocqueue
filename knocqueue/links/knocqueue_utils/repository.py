import abc
from flask_sqlalchemy.model import Model
from typing import TypeVar, Generic, Union
T = TypeVar('T', bound=Model)


class Repository(Generic[T], metaclass=abc.ABCMeta):
    _model: T = None

    @classmethod
    def get_by_pk(cls, pk) -> Union[T, None]:
        return cls._model.query.get(pk)
