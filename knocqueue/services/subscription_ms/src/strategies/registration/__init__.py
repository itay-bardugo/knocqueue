import abc
from typing import Type
from src.models import Subscription
from src.repositories.subscription import SubscriptionRepository


class RegistrationStrategy(metaclass=abc.ABCMeta):
    def __init__(self):
        self._repository: Type[SubscriptionRepository] = SubscriptionRepository

    @abc.abstractmethod
    def register(self, subscription: Subscription):
        ...
