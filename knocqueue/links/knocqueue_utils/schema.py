from marshmallow import Schema, fields, ValidationError, INCLUDE, validates_schema, post_load
from knocqueue_utils.interfaces.when import IWhen, When, Expression
import abc

fields.Field.default_error_messages |= {
    "required": "ms-required",
    "null": 'ms-null',
}


class CustomInvalidError:
    default_error_messages = {
        "invalid": "ms-invalid",
    }


class Email(CustomInvalidError, fields.Email):
    ...


class Str(CustomInvalidError, fields.Str):
    ...


class Bool(CustomInvalidError, fields.Bool):
    ...


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

    def _on_post_load(self, data, **kwargs):
        ...

    @post_load
    def _post_load(self, data, **kwargs):
        return self._on_post_load(data, **kwargs)
