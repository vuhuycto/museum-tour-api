from functools import wraps

import marshmallow
import werkzeug.exceptions
from flask import request

from main.commons.exceptions import Unauthorized
from main.engines.ticket import find_ticket_by_id
from main.enums import HttpElement
from main.libs.jwt import get_jwt_data, get_jwt_token
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


def require_not_expired_ticket(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = get_jwt_token()
        data = get_jwt_data(token)
        ticket = find_ticket_by_id(data["id"]) if data is not None else None

        if ticket and not ticket.expired:
            kwargs["ticket"] = ticket
            return f(*args, **kwargs)
        else:
            raise Unauthorized()

    return wrapper
