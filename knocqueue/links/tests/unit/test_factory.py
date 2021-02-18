from unittest import TestCase
from unittest.mock import patch, MagicMock
from knocqueue_utils.factories import Factory, Builder


class Factory_(Factory):
    ...


class B(Builder):

    def __call__(self, *args, **kwargs):
        return 'ok'


class TestFactory(TestCase):
    def test_it_can_not_be_instantiated(self):
        with self.assertRaises(TypeError) as ctx:
            Factory()

    def test_it_can_be_inherited(self):
        try:
            Factory_()
        except TypeError:
            self.fail()

    def test_it_registers_and_returns(self):
        ...
