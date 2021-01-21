from . import Repository
from src.models import Subscription
from typing import Union


class SubscriptionRepository(Repository):
    _model = Subscription

    @classmethod
    def get_by_id(cls, id_) -> Union[None, Subscription]:
        return super().get_by_id(id_)

