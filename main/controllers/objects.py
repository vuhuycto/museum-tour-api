from main import app
from main.commons.exceptions import NotFound
from main.engines.object import find_object_by_identifier
from main.schemas.object import ObjectSchema


@app.route("/objects/<object_identifier>", methods=["GET"])
def get_museum_object(object_identifier):
    obj = find_object_by_identifier(object_identifier)

    if obj is None:
        raise NotFound(error_message=f"{object_identifier} not found.")

    return ObjectSchema().jsonify(obj)
