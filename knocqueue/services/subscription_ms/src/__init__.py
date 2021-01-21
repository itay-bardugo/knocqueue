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
