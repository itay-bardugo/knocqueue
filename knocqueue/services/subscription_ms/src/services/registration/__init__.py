from src.repositories import Repository
from src.strategies.registration import RegistrationStrategy


class RegisterService:
    def __init__(self, repository: Repository, strategy: RegistrationStrategy):
        self._repository = repository
        self._strategy = strategy

    def _validate(self):
        ...

    def execute(self):
        self._validate()
        return self._register()

    def _register(self):
        return self._strategy.register()
