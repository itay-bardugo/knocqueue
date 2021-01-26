from flask_restful import Resource
from src.boot.registration_factories import factory
from src.http.schema.subscription import CredentialsRegistrationSchema
from flask import request
from marshmallow import ValidationError


class Subscription(Resource):
    # key is the method, value is the factory alias
    __map = {
        'simple': 'credentials'
    }

    def get(self, method):
        try:
            register = factory.make(Subscription.__map[method])
            return register.register(request.args)
        except ValidationError as e:
            return e.messages, 400
        except KeyError:
            return 'Bad Request', 400

    # def get(self):
    #     return 'get'
