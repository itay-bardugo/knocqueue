from src.repositories.subscription import SubscriptionRepository
from marshmallow import Schema, fields, ValidationError, INCLUDE, validates_schema
from typing import Type
from knocqueue_utils.statement import When


class Registration(Schema):
    class Meta:
        unknown = INCLUDE

    email = fields.Email(required=True, data_key='email')
    password = fields.Str(required=True, data_key='password')
    allow_news_letter = fields.Bool(required=False, data_key='allowNewsLetter')

    def __init__(self, **kwargs):
        self.__repository: Type[SubscriptionRepository] = kwargs.pop('repository')
        super().__init__(**kwargs)

    @validates_schema
    def validate_registration(self, data, **kwargs):
        When(self.__repository.get_by_email(data['email'])) \
            .happens() \
            .then \
            .raise_an_error(ValidationError({'code': 405}))


class CredentialsRegistrationSchema(Registration):
    ...
