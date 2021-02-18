from unittest import TestCase
from src.main import app


class BaseTestCase(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
