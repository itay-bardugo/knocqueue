from unittest import TestCase
from unittest.mock import patch, MagicMock
from knocqueue_utils.factories import Factory, Builder


class FactoryTest(Factory[int]):
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
            FactoryTest()
        except TypeError:
            self.fail()

    def test_it_runs_the_builder(self):
        builder = B()

        with patch.object(type(builder), '__call__') as mock:
            f = FactoryTest()
            f.register('test', builder)
            f.make('test')
            mock.assert_called()
