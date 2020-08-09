import uuid

from db import db


class User_Model(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.password = password

    def json(self):
        return {
            "user_id": self.user_id,
            "username": self.username
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
