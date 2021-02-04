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

    def post(self, method):
        from flask import abort
        from marshmallow.fields import Field, FieldABC

        def get_all_subclasses(cls):
            all_subclasses = []

            for subclass in cls.__subclasses__():
                all_subclasses.append(subclass)
                all_subclasses.extend(get_all_subclasses(subclass))

            return all_subclasses

        abort({i: v.default_error_messages | {'nameCLS': str(v)} for i, v in enumerate(get_all_subclasses(Field))})
        try:
            register = factory.make(Subscription.__map[method])
            return register.execute(request.args)
        except ValidationError as e:
            return e.messages, 400
        except KeyError as e:
            return 'Bad Request!', 400

