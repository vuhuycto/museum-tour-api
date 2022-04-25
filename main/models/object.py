from sqlalchemy_utils import URLType

from main import db


class ObjectModel(db.Model):
    __tablename__ = "object"

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100), nullable=False)
    description_url = db.Column(URLType, nullable=False)

    def __str__(self):
        return self.name
