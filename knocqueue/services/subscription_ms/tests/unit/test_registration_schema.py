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
        with self.assertRaises(ValidationError):
            self.registration_schema.load({'email': 'test@test.com'})

        with self.assertRaises(ValidationError):
            self.registration_schema.load({'password': '123456'})

        with self.assertRaises(ValidationError):
            self.registration_schema.load({'first_name': 'test'})

        with self.assertRaises(ValidationError):
            self.registration_schema.load({'last_name': 'test'})

    def test_it_accepts_all_required_inputs(self):
        try:
            self.registration_schema.validate({
                'email': 'test@test.com',
                'password': '123456',
                'first_name': 'test',
                'last_name': 'test'
            })
        except ValidationError as v:
            print(str(v))
            self.fail()
