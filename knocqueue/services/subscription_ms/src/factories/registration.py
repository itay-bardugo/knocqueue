from knocqueue_utils.factories import (Factory, Builder)
from src.services.registration import RegisterService
from src.strategies.registration.credentials import RegisterWithCredentialsStrategy
from src.repositories.subscription import SubscriptionRepository


class RegistrationFactory(Factory):
    def make(self, method, *args, **kwargs) -> RegisterService:
        return super().make(method, *args, **kwargs)


class CredentialsBuilder(Builder):

    def __call__(self, *args, **kwargs):
        return RegisterService(
            SubscriptionRepository(),
            RegisterWithCredentialsStrategy()
        )
