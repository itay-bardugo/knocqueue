from src.repositories.subscription import SubscriptionRepository
from typing import Type
from knocqueue_utils import schema
from marshmallow import ValidationError, validate


class Registration(schema.BaseSchema):
    email = schema.Email(required=True, data_key='email')
    password = schema.Str(required=True, validate=[validate.Length(min=6, max=16, error='ms-password-length')],
                          data_key='password')
    allow_news_letter = schema.Bool(required=False, data_key='allowNewsLetter')
    _repository: Type[SubscriptionRepository]

    def validate_schema(self, data, **kwargs):
        self.when(self._repository.get_by_email(data['email'])) \
            .happens() \
            .then \
            .raise_an_error(ValidationError('ms-user-exists'))

    def _on_post_load(self, data, **kwargs):
        #return SubscriptionRepository.model
        ...


class CredentialsRegistrationSchema(Registration):
    ...
