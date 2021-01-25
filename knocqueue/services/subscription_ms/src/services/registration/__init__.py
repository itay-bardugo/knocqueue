from src.repositories import Repository
from src.strategies.registration import RegistrationStrategy
from marshmallow import Schema


class RegisterService:
    def __init__(self, repository: Repository, strategy: RegistrationStrategy, schema: Schema):
        self._repository = repository
        self._strategy = strategy
        self._schema = schema

    def _validate(self, payload):
        self._schema.load(payload)  # validate the payload

    def register(self, payload: dict):
        self._validate(payload)
        return self._register()

    def _register(self):
        return self._strategy.register()
