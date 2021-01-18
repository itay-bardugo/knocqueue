from flask_restful import Resource


class Subscription(Resource):
    def post(self):
        return 'hi'

    def get(self):
        import sys
        return str(sys.path)
