from knocqueue_utils.statement import When, Expression
import abc


class IWhen:
    @abc.abstractmethod
    def when(self, expression) -> Expression:
        ...
