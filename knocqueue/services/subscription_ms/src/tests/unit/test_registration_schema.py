from . import BaseTestCase
from unittest import TestCase
from unittest.mock import patch
from src.http.schema.subscription import CredentialsRegistrationSchema, SubscriptionRepository
from marshmallow import ValidationError


class TestCredentialsSchema(TestCase):
    def setUp(self) -> None:
        self.schema = CredentialsRegistrationSchema(repository=SubscriptionRepository)

    @patch('src.http.schema.subscription.SubscriptionRepository.filter_by_first')
    def test_it_doesnt_fail_when_email_not_exist(self, filter_by_first):
        filter_by_first.return_value = None
        self.schema._email_not_exists()

    @patch('src.http.schema.subscription.SubscriptionRepository.filter_by_first')
    def test_it_does_fail_when_email_not_exist(self, filter_by_first):
        filter_by_first.return_value = True
        with self.assertRaises(ValidationError):
            self.schema._email_not_exists('test')