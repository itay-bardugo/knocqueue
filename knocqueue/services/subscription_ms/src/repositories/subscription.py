from . import Repository
from src.models import Subscription


class SubscriptionRepository(Repository[Subscription]):
    _model = Subscription
