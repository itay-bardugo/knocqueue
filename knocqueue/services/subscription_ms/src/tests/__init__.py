from unittest import TestCase
from src.main import app
from flask import Response


class BaseTestCase(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.response = lambda *args, **kwargs: Response(*args, **kwargs)
