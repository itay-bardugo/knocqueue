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

    @validates_schema
    def _validate_schema(self, data, **kwargs):
        return self.validate_schema(data, **kwargs)

    @abc.abstractmethod
    def validate_schema(self, data, **kwargs):
        ...
