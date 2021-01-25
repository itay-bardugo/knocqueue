from src import api, app
from src.http.controllers import (Subscription)

api.add_resource(Subscription, '/subscription', '/subscription/register/<string:method>')


@app.before_request
def on_init():
    ...


@app.teardown_request
def on_teardown(x):
    ...
