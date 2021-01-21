from . import Factory, Builder, DTO
from src.services.registration.credentials import RegisterService
from src.services.registration.credentials import RegisterWithCredentialsService
from src.repositories.subscription import SubscriptionRepository


class RegistrationFactory(Factory):
    def make(self, method, *args, **kwargs) -> RegisterService:
        return super().make(method, *args, **kwargs)


class CredentialsBuilder(Builder):

    def __call__(self, *args, **kwargs):
        return RegisterWithCredentialsService(
            SubscriptionRepository(), *args, **kwargs
        )
