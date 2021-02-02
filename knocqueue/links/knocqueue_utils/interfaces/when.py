import abc
from typing import Type
from knocqueue_utils.statement import When


class IWhen(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def when(self) -> Type[When]:
        ...
