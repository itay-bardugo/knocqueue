import abc
from flask_sqlalchemy.model import Model
from flask_sqlalchemy import SQLAlchemy
from typing import TypeVar, Generic, Union, Type, List

T = TypeVar('T', bound=Model)
_DB = TypeVar('_DB', bound=SQLAlchemy)


class Repository(Generic[T], metaclass=abc.ABCMeta):
    _model: Type[T] = None
    _db_session: _DB = None

    @classmethod
    def get_by_pk(cls, pk) -> Union[T, None]:
        return cls._model.query.get(pk)

    @classmethod
    def filter_by_first(cls, **kwargs) -> Union[T, None]:
        return cls._model.query.filter_by(**kwargs).first()

    @classmethod
    def filter_by_all(cls, **kwargs) -> List[T]:
        return cls._model.query.filter_by(**kwargs).all()

    @classmethod
    def insert(cls, model: T, commit=True):
        cls._db_session.session.add(model)
        if commit:
            cls._db_session.session.commit()
        return model
