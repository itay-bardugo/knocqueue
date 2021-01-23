import abc


class RegistrationStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register(self):
        ...
