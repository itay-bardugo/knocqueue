from . import app
from jwcrypto import jwk, jwe, jws, jwt
from jwcrypto.common import json_encode
from authentication import settings


@app.route('/')
def index():
    return 'hi!'
