import abc
from typing import Type
from flask_sqlalchemy.model import Model
from src.repositories.subscription import SubscriptionRepository
from marshmallow import Schema, fields, ValidationError, INCLUDE, validates_schema
from knocqueue_utils.statement import When


class BaseSchema(Schema):
    class Meta:
        unknown = INCLUDE

    def __init__(self, **kwargs):
        self.__repository: Type[SubscriptionRepository] = kwargs.pop('repository')
        super().__init__(**kwargs)

    def _when(self) -> Type[When]:
        return When

    @abc.abstractmethod
    @validates_schema
    def validate_registration(self, data, **kwargs):
        When(self.__repository.get_by_email(data['email'])) \
            .happens() \
            .then \
            .raise_an_error(ValidationError({'code': 405}))


class Registration(BaseSchema):
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


class Repository(metaclass=abc.ABCMeta):
    _model: Model = None

    @classmethod
    def get_by_id(cls, id_):
        return cls._model.query.filter_by(id=id_).first()


class Process(metaclass=abc.ABCMeta):
    def __init__(self, *, repository: Type[Repository], strategy: RegistrationStrategy, schema: Type[Registration],
                 **kwargs):
        self._repository = repository
        self._strategy = strategy
        self._schema = schema(repository=self._repository)

    def _validate(self, payload):
        self._schema.load(payload)  # validate the payload

    @abc.abstractmethod
    def execute(self, payload: dict):
        self._validate(payload)
        return self._register()

    def _register(self):
        return self._strategy.register()
