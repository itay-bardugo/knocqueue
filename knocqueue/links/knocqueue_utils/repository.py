import abc
from flask_sqlalchemy.model import Model
from typing import TypeVar, Generic, Union, Type, List

T = TypeVar('T', bound=Model)


class Repository(Generic[T], metaclass=abc.ABCMeta):
    _model: Type[T] = None

    @classmethod
    def get_by_pk(cls, pk) -> Union[T, None]:
        return cls._model.query.get(pk)

    @classmethod
    def filter_by_first(cls, **kwargs) -> Union[T, None]:
        return cls._model.query.filter_by(**kwargs).first()

    @classmethod
    def filter_by_all(cls, **kwargs) -> List[T]:
        return cls._model.query.filter_by(**kwargs).all()
