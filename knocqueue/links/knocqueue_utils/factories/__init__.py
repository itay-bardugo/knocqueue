import abc
from typing import TypeVar, Generic

T = TypeVar('T')


class Factory(Generic[T]):
    def __new__(cls):
        if cls is Factory:
            raise TypeError("Can't instantiate abstract class {}".format(Factory.__name__))
        return super().__new__(cls)

    def __init__(self):
        self._builders = {}

    def register(self, method, builder: 'Builder'):
        self._builders[method] = builder

    def make(self, method, *args, **kwargs) -> T:
        return self._builders[method](*args, **kwargs)


class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        ...
