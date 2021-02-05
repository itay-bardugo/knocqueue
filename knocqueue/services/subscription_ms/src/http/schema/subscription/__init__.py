from src.repositories.subscription import SubscriptionRepository
from typing import Type
from knocqueue_utils.schema import BaseSchema
from marshmallow import fields, ValidationError


class Registration(BaseSchema):
    email = fields.Email(required=True, data_key='email')
    password = fields.Str(required=True, data_key='password')
    allow_news_letter = fields.Bool(required=False, data_key='allowNewsLetter')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._repository: Type[SubscriptionRepository]

    def validate_schema(self, data, **kwargs):
        self.when(self._repository.get_by_email(data['email'])) \
            .happens() \
            .then \
            .raise_an_error(ValidationError({'code': 405}))


class CredentialsRegistrationSchema(Registration):
    ...
