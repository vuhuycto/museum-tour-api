from functools import wraps

import marshmallow
import werkzeug.exceptions
from flask import request

from main.enums import HttpElement
from main.schemas.base import BaseSchema

from .exceptions import BadRequest, ValidationError


def validate_request(http_element: HttpElement, schema: BaseSchema):
    def validate_request_decorator(f):
        @wraps(f)
        def validate_request_wrapper(*args, **kwargs):
            try:
                if http_element is HttpElement.BODY:
                    kwargs["data"] = schema.load(request.get_json())
                elif http_element is HttpElement.QUERY:
                    kwargs["query"] = schema.load(request.args.to_dict())
                return f(*args, **kwargs)
            except werkzeug.exceptions.BadRequest as e:
                raise BadRequest(error_message=e.description)
            except marshmallow.ValidationError as e:
                raise ValidationError(error_data=e.messages)

        return validate_request_wrapper

    return validate_request_decorator
