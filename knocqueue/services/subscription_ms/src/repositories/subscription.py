from knocqueue_utils.repository import Repository
from src.models import Subscription
from typing import Union


class SubscriptionRepository(Repository[Subscription]):
    _model = Subscription

    @classmethod
    def get_by_email(cls, email) -> Union[None, Subscription]:
        return cls._model.query.filter_by(email=email).first()

