import abc
from typing import Type, Generic, TypeVar
from knocqueue_utils.schema import BaseSchema
from knocqueue_utils.repository import Repository

_Repository = TypeVar('_Repository', bound=Repository)
_Schema = TypeVar('_Schema', bound=BaseSchema)
_Model = TypeVar('_Model')


class Process(Generic[_Model], metaclass=abc.ABCMeta):
    def __init__(self, *, repository: Type[_Repository], schema: Type[_Schema]):
        self._repository = repository
        self._schema = schema(repository=self._repository)
        self.__model: _Model = None

    def _validate(self, payload):
        self.__model = self._schema.load(payload)  # validate the payload

    def model(self) -> _Model:
        return self.__model

    def execute(self, payload: dict):
        self._validate(payload)
        return self._execute()

    @abc.abstractmethod
    def _execute(self):
        ...
