from typing import Callable, Any
import abc


class _BaseThen(metaclass=abc.ABCMeta):
    def __init__(self, checks: set):
        self._confirmed = any(checks)
        self._flag = False

    def _do_if_confirmed(self, callable_: Callable[..., Any]):
        if self._flag:
            raise Exception('--preventing from executing twice--')

        if self._confirmed:
            self._flag = True
            return callable_()

    def raise_an_error(self, exception: BaseException):
        def _():
            raise exception

        self._do_if_confirmed(_)
        return self


class _Otherwise(_BaseThen):
    ...


class _Then(_BaseThen):
    @property
    def otherwise(self):
        return _Otherwise({True if self._flag is False else False})


class _Expression:
    def __init__(self):
        self._checks = set()
        self.value = None

    def _setup(self):
        self.__init__()
        return self

    def _happens(self):
        return bool(self.value)

    def happens(self):
        self._add_check(self._happens())
        return self

    def _add_check(self, expression):
        self._checks.add(expression)

    def not_happens(self):
        self._add_check(not self._happens())

    @property
    def then(self):
        return _Then(self._checks)


class When(type):
    _expression = _Expression()

    def __new__(mcs, expression) -> _Expression:
        if mcs._expression is None:
            mcs._expression = mcs._Expression()
        mcs._expression._setup()
        mcs._expression.value = expression
        return mcs._expression

    def kill(cls):
        cls._expression = None

Expression = _Expression