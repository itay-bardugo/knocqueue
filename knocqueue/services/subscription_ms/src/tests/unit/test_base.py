import unittest
from src import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.post('/subscription/register/a', follow_redirects=True)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

