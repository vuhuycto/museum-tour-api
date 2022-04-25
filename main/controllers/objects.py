from main import app
from main.commons.decorators import require_not_expired_ticket
from main.commons.exceptions import NotFound
from main.engines.object import find_object_by_identifier
from main.schemas.object import ObjectSchema


@app.get("/objects/<object_identifier>")
@require_not_expired_ticket
def get_museum_object(object_identifier, **__):
    obj = find_object_by_identifier(object_identifier)

    if obj is None:
        raise NotFound(error_message=f"{object_identifier} not found.")

    return ObjectSchema().jsonify(obj)
