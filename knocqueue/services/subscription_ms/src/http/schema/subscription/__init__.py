from src.repositories.subscription import SubscriptionRepository
from marshmallow import Schema, fields, ValidationError, INCLUDE, validates_schema, types


class _Registration(Schema):
    class Meta:
        unknown = INCLUDE

    email = fields.Email(required=True, data_key='email')
    password = fields.Str(required=True, data_key='password')
    allow_news_letter = fields.Int(required=False, data_key='allowNewsLetter')

    def __init__(self, **kwargs):
        self.__repository: SubscriptionRepository = kwargs.pop('repository')
        super().__init__(**kwargs)

    @validates_schema
    def validate_registration(self, data, **kwargs):
        if self.__repository.get_by_email(data['email']) is not None:
            raise ValidationError('user already exists')


class CredentialsRegistrationSchema(_Registration):
    ...
