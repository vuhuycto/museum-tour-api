from typing import Optional

from main import db
from main.models.ticket import TicketModel


def create_ticket(transaction_id: str) -> TicketModel:
    ticket = TicketModel(transaction_id=transaction_id)
    db.session.add(ticket)
    db.session.commit()

    return ticket


def find_ticket_by_id(ticket_id: str) -> Optional[TicketModel]:
    ticket = TicketModel.query.filter(TicketModel.id == ticket_id).first()
    return ticket


def destroy_ticket(ticket: TicketModel) -> None:
    ticket.expired = True
    db.session.commit()
