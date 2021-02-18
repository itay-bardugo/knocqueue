from src.tests import BaseTestCase
from unittest.mock import patch, MagicMock


class TestRegistration(BaseTestCase):
    @patch('src.routes.Subscription.post')
    def test_it_responds_with_200_on_simple_registration(self, registration_endpoint):
        registration_endpoint.return_value = self.response('OK')
        response = self.app.post('/subscription/register/simple')
        self.assertEqual(200, response.status_code)

    @patch.dict('src.routes.Subscription._Subscription__map', {'pass': 'pass'})
    def test_it_responds_with_404_on_undefined_registration_type(self):
        response = self.app.post('/subscription/register/invalid')
        self.assertEqual(404, response.status_code)
