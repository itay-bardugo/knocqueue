from knocqueue_utils.e2e.process import Process
from src.strategies.registration import RegistrationStrategy
from src.models import Subscription


class RegisterService(Process[Subscription]):

    def __init__(self, **kwargs):
        self._strategy: RegistrationStrategy = kwargs.pop('strategy')
        super().__init__(**kwargs)

    def _execute(self):
        return self._strategy.register()
