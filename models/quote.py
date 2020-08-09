import uuid

from db import db
from sqlalchemy import func


class Quote_Model(db.Model):

    __tablename__ = "quotes"

    quote_id = db.Column(db.String(100), primary_key=True)
    quote_description = db.Column(db.String(1000))
    quote_author = db.Column(db.String(80))

    def __init__(self, quote_description, quote_author):
        self.quote_id = str(uuid.uuid4())
        self.quote_description = quote_description
        self.quote_author = quote_author

    def json(self):
        return {
            "quote_id": self.quote_id,
            "quote_description": self.quote_description,
            "quote_author": self.quote_author
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_random_quote(cls):
        return cls.query.order_by(func.random()).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def get_quote_by_id(cls, quote_id):
        return cls.query.filter_by(quote_id=quote_id).first()
