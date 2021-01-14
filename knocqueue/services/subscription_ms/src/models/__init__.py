from src import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
    last_update = db.Column(db.TIMESTAMP, server_default=db.func.now(), onupdate=db.func.current_timestamp())
