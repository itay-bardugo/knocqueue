import abc
from typing import Type
from knocqueue_utils.schema import BaseSchema
from knocqueue_utils.repository import Repository


class Process(metaclass=abc.ABCMeta):
    def __init__(self, *, repository: Type[Repository], schema: Type[BaseSchema]):
        self._repository = repository
        self._schema = schema(repository=self._repository)

    def _validate(self, payload):
        self._schema.load(payload)  # validate the payload

    def execute(self, payload: dict):
        self._validate(payload)
        return self._execute()

    @abc.abstractmethod
    def _execute(self):
        ...
