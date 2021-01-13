from . import app
from jwcrypto import jwk, jwe, jws, jwt
from jwcrypto.common import json_encode, json_decode
from authentication import settings
from flask import request


@app.route('/')
def index():
    public_file = (open(str(settings.ROOT) + "/public.pub", "r"))
    public_key = jwk.JWK.from_pem(public_file.read().encode())
    ks = jwk.JWKSet()
    ks.add(public_key)
    return ks.export(as_dict=True)

    ks2 = jwk.JWKSet()
    ks2.import_keyset(ks.export(False))
    kkk = ks2.get_key(public_key.key_id)
    return kkk.export_to_pem(True, None)


@app.route("/keyPairs")
def make_key_pairs():
    k = jwk.JWK.generate(kty='RSA')
    private = k.export_to_pem(True, None)
    public = k.export_to_pem()

    with open(settings.ROOT + '/public.pub', 'w') as f:
        f.write(public.decode('utf-8'))

    with open(settings.ROOT + '/private.pem', 'w') as f:
        f.write(private.decode('utf-8'))

    return "ok"


@app.route("/encrypt")
def encrypt():
    public_file = (open(str(settings.ROOT) + "/public.pub", "r"))
    private_file = (open(str(settings.ROOT) + "/private.pem", "r"))
    public_key = jwk.JWK.from_pem(public_file.read().encode())
    private_key = jwk.JWK.from_pem(private_file.read().encode())

    import time
    t = round(time.time()) + 10
    payload = {"exp": t, "data": {'itay': 'itay'}}
    header = {"alg": "RS256", "kid": private_key.thumbprint()}
    jwttoken = jwt.JWT(header=header, claims=payload)
    jwttoken.make_signed_token(private_key)
    payload = jwttoken.serialize(True)

    encrypt_header = {"kid": private_key.thumbprint(), "alg": "RSA-OAEP", "enc": "A128CBC-HS256"}
    jwttoken_e = jwt.JWT(header=encrypt_header, claims=payload)
    jwttoken_e.make_encrypted_token(public_key)
    payload = jwttoken_e.serialize(True)

    return payload


@app.route("/decrypt")
def decrypt():
    public_file = (open(str(settings.ROOT) + "/public.pub", "r"))
    private_file = (open(str(settings.ROOT) + "/private.pem", "r"))
    public_key = jwk.JWK.from_pem(public_file.read().encode())
    private_key = jwk.JWK.from_pem(private_file.read().encode())
    enc = request.args.get("k")

    e = jwt.JWT(key=private_key, jwt=enc)
    s = jwt.JWT()
    s.leeway = 999999
    s.deserialize(jwt=e.claims, key=public_key)

    # it can be validated from keyset
    #ks = jwk.JWKSet()
    #ks.import_keyset(json_encode(index()))
    #s.deserialize(jwt=e.claims, key=ks.get_key(json_decode(e.header)["kid"]))


    return json_decode(s.claims)
