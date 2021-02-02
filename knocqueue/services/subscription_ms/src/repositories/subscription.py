from knocqueue_utils.repository import Repository
from src.models import Subscription
from typing import Union


class SubscriptionRepository(Repository):
    _model = Subscription

    @classmethod
    def get_by_pk(cls, pk) -> Union[None, Subscription]:
        return super().get_by_pk(pk)

    @classmethod
    def get_by_email(cls, email) -> Union[None, Subscription]:
        return cls._model.query.filter_by(email=email).first()
