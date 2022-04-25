from flask_admin.contrib.sqla import ModelView

from main import admin, db
from main.models.object import ObjectModel
from main.models.ticket import TicketModel

object_model_view = ModelView(
    ObjectModel,
    db.session,
    name="Object",
)
ticket_model_view = ModelView(
    TicketModel,
    db.session,
    name="Ticket",
)

admin.add_view(object_model_view)
admin.add_view(ticket_model_view)
