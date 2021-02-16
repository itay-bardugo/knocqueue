from knocqueue_utils.repository import Repository as _Repository
from src import db
from typing import TypeVar

_T = TypeVar('_T')


class Repository(_Repository[_T]):
    _db_session = db
