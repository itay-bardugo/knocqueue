import abc
from src.repositories import Repository


class RegisterService(metaclass=abc.ABCMeta):
    def __init__(self, repository: Repository, *args, **kwargs):
        self._repository = repository

    @abc.abstractmethod
    def register(self):
        ...
