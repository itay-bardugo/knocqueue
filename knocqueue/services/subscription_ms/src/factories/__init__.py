import abc


class DTO(metaclass=abc.ABCMeta):
    ...


class Factory(metaclass=abc.ABCMeta):
    def __init__(self):
        self._builders = {}

    def register(self, method, builder):
        self._builders[method] = builder

    def make(self, method, *args, **kwargs):
        return self._builders[method](*args, **kwargs)


class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, dto: DTO):
        ...
