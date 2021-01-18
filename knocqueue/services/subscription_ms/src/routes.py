from src import api
from src.rest.controllers import (Subscription)


api.add_resource(Subscription, '/')
