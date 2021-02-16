from src import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.event import listens_for
import hashlib
import uuid


class Subscription(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
    allow_news_letter = db.Column(db.Boolean, default=False)
    last_update = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.current_timestamp())


@listens_for(Subscription, 'before_insert')
def _salting(mapper, connection, target: Subscription):
    if target.password:
        target.password = hashlib.md5(target.password.encpde).hexdigest()