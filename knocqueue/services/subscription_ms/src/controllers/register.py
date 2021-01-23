from flask_restful import Resource
from src.boot.registration_factories import factory


class Register(Resource):
    # key is the method, value is the factory alias
    __map = {
        'simple': 'credentials'
    }

    def post(self, method):
        try:
            register = factory.make(Register.__map[method])
            return register.execute()
        except KeyError:
            return 'Bad Request', 400
