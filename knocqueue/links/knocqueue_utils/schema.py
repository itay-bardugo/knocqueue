from marshmallow import Schema, fields, ValidationError, INCLUDE, validates_schema
from knocqueue_utils.interfaces.when import IWhen, When, Expression
import abc


class BaseSchema(Schema, IWhen):
    class Meta:
        unknown = INCLUDE

    def __init__(self, **kwargs):
        self._repository = kwargs.pop('repository')
        super().__init__(**kwargs)

    def when(self, expression) -> Expression:
        return When(expression)

    @abc.abstractmethod
    @validates_schema
    def validate_registration(self, data, **kwargs):
        ...
