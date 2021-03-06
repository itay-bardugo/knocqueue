from knocqueue_utils.factories import (Factory, Builder)
from src.services.registration import RegisterService
from src.strategies.registration.credentials import RegisterWithCredentialsStrategy
from src.repositories.subscription import SubscriptionRepository
from src.http.schema.subscription import CredentialsRegistrationSchema


class RegistrationFactory(Factory[RegisterService]):
    ...


class CredentialsBuilder(Builder):

    def __call__(self, *args, **kwargs):
        return RegisterService(
            repository=SubscriptionRepository,
            strategy=RegisterWithCredentialsStrategy(),
            schema=CredentialsRegistrationSchema
        )
