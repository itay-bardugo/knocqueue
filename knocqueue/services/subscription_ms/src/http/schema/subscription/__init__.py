from marshmallow import Schema, fields, ValidationError


class _Registration(Schema):
    email = fields.Email(required=True, data_key='email')
    password = fields.Str(required=True, data_key='password')
    allow_news_letter = fields.Int(required=False, data_key='allowNewsLetter')


class CredentialsRegistrationSchema(_Registration):
    ...
