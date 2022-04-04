from flask_admin.contrib.sqla import ModelView

from main import admin, db
from main.models.object import ObjectModel

object_model_view = ModelView(
    ObjectModel,
    db.session,
    name="Object",
)

admin.add_view(object_model_view)
