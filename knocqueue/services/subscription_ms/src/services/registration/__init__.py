from knocqueue_utils.e2e.process import Process
from src.strategies.registration import RegistrationStrategy


class RegisterService(Process):

    def __init__(self, **kwargs):
        self._strategy: RegistrationStrategy = kwargs.pop('strategy')
        super().__init__(**kwargs)

    def _execute(self):
        return self._strategy.register()

#
# class RegisterService2:
#     def __init__(self, repository: Type[Repository], strategy: RegistrationStrategy, schema: Type[Registration]):
#         self._repository = repository
#         self._strategy = strategy
#         self._schema = schema(repository=self._repository)
#
#     def _validate(self, payload):
#         self._schema.load(payload)  # validate the payload
#
#     def register(self, payload: dict):
#         self._validate(payload)
#         return self._register()
#
#     def _register(self):
#         return self._strategy.register()
