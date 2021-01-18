import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from src import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_CONNECTION_STRING", "")
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=settings.MIGRATION_PATH)
api = Api(app)


# todo: model properly
class ServiceToServiceHandshakeMiddleWare:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        import os
        import requests
        requests.post(
            os.environ.get("AUTHENTICATION_SERVICE_TO_SERVICE_VERIFY_ENDPOINT"),
        )
