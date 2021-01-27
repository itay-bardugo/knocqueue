from src.repositories import Repository
from src.strategies.registration import RegistrationStrategy
from src.http.schema.subscription import Registration
from typing import Type


class RegisterService:
    def __init__(self, repository: Type[Repository], strategy: RegistrationStrategy, schema: Type[Registration]):
        self._repository = repository
        self._strategy = strategy
        self._schema = schema(repository=self._repository)

    def _validate(self, payload):
        self._schema.load(payload)  # validate the payload

    def register(self, payload: dict):
        self._validate(payload)
        return self._register()

    def _register(self):
        return self._strategy.register()
