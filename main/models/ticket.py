from main import db


class TicketModel(db.Model):
    __tablename__ = "ticket"

    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(20), nullable=False)
    expired = db.Column(db.Boolean, default=False)
