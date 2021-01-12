from django.shortcuts import render, HttpResponse

from jwcrypto import jwk, jwe, jws, jwt
from jwcrypto.common import json_encode
from console import settings


# Create your views here.
def encrypt(request):
    public_file = (open(str(settings.BASE_DIR) + "/public.pub", "r"))
    private_file = (open(str(settings.BASE_DIR) + "/private.pem", "r"))
    public_key = jwk.JWK.from_pem(public_file.read().encode())
    private_key = jwk.JWK.from_pem(private_file.read().encode())

    # payload = json_encode()
    import time
    t = round(time.time()) + 10
    payload = {"exp": t, "sub": json_encode({'itay': 'itay'})}

    header = {"alg": "RS256", "kid": private_key.thumbprint()}
    jwttoken = jwt.JWT(header=header, claims=payload)
    jwttoken.make_signed_token(private_key)
    payload = jwttoken.serialize(True)

    encrypt_header = {"alg": "RSA-OAEP", "enc": "A128CBC-HS256"}
    jwttoken_e = jwt.JWT(header=encrypt_header, claims=payload)
    jwttoken_e.make_encrypted_token(public_key)
    payload = jwttoken_e.serialize(True)

    return HttpResponse(payload)


def decrypt(request):
    public_file = (open(str(settings.BASE_DIR) + "/public.pub", "r"))
    private_file = (open(str(settings.BASE_DIR) + "/private.pem", "r"))
    public_key = jwk.JWK.from_pem(public_file.read().encode())
    private_key = jwk.JWK.from_pem(private_file.read().encode())
    enc = request.GET.get("k")

    e = jwt.JWT(key=private_key, jwt=enc)
    s = jwt.JWT()
    s.leeway = 0
    s.deserialize(jwt=e.claims, key=public_key)
    return HttpResponse(s.claims)
