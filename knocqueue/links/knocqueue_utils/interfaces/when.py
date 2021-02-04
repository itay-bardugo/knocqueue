from knocqueue_utils.statement import When, Expression
import abc


class IWhen(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def when(self, expression) -> Expression:
        ...
