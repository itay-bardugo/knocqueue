from unittest import TestCase
from unittest.mock import patch
from src.http.schema.subscription import CredentialsRegistrationSchema, SubscriptionRepository
from marshmallow import ValidationError


class TestRegistrationSchema(TestCase):
    def setUp(self) -> None:
        self.registration_schema = CredentialsRegistrationSchema(repository=SubscriptionRepository)

    @patch('src.http.schema.subscription.SubscriptionRepository.filter_by_first')
    def test_it_doesnt_fail_when_email_not_exist(self, filter_by_first):
        filter_by_first.return_value = None
        self.registration_schema._email_not_exists('test')

    @patch('src.http.schema.subscription.SubscriptionRepository.filter_by_first')
    def test_it_fails_when_email_not_exist(self, filter_by_first):
        filter_by_first.return_value = True
        with self.assertRaises(ValidationError):
            self.registration_schema._email_not_exists('test')

    def test_it_fails_on_missing_inputs(self):
        self.assertTrue(self.registration_schema.validate({'email': 'test@test.com'}))

        self.assertTrue(self.registration_schema.validate({'password': '123456'}))

        self.assertTrue(self.registration_schema.validate({'first_name': 'test'}))

        self.assertTrue(self.registration_schema.validate({'last_name': 'test'}))

    def test_it_accepts_all_required_inputs(self):
        with patch.object(self.registration_schema, 'validate_schema') as mock:
            mock.return_value = True
            errors = self.registration_schema.validate({
                'email': 'test@test.com',
                'password': '123456',
                'first_name': 'test',
                'last_name': 'test'
            })
            self.assertFalse(errors)
