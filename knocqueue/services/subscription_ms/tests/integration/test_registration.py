from tests import BaseTestCase
from unittest.mock import patch


class TestRegistration(BaseTestCase):
    @patch('src.factories.registration.RegisterService.execute')
    def test_it_responds_200_on_simple_registration(self, registration_endpoint):
        registration_endpoint.return_value = self.response('OK')
        response = self.app.post('/subscription/register/simple')
        self.assertEqual(200, response.status_code)

    @patch.dict('src.routes.Subscription._Subscription__map', {'pass': 'pass'}, clear=True)
    def test_it_responds_404_on_undefined_registration_type(self):
        response = self.app.post('/subscription/register/invalid')
        self.assertEqual(404, response.status_code)
