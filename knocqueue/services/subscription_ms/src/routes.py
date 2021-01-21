from src import api, app
from src.controllers import (Register)

api.add_resource(Register, '/register/<string:method>')


@app.before_request
def on_init():
    ...


@app.teardown_request
def on_teardown(x):
    ...
